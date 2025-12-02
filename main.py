from modulefinder import test
import pickle
import chromadb
from chromadb.config import Settings   #used only to configure how ChromaDB should run and how or where it should store/retrieve data from


###
#loadinggg... files
###
EMBEDDINGS_PICKLE = "embeddings.pkl"  #local embeddings file

with open(EMBEDDINGS_PICKLE, "rb") as f:
    saved_data = pickle.load(f)

vector = [emb[1] for emb in saved_data["embeddings"]]  #extracting only the vectors  
book_texts = book_texts = [text for (_, text) in saved_data["titles"]]    #only the string text from (id, text) tuples

print("loaded embeddings for", len(book_texts), "books.") 

#testing
# print(type(book_embeddings[0]))
# print(book_embeddings[0])



###
#connectinggg... db
###
#creates a Chroma database stored locally
client = chromadb.PersistentClient(path="chroma_db") #connects to the existing database named "chroma_db" (if exists or else creates one)      


collection_name = "books"  #collection that stores book embeddings from save_embeddings_into_chroma.py
#if collection exists then load it
if collection_name in [c.name for c in client.list_collections()]:  #goes through each collection object c in the list returned by client.list_collections() and extracts its .name which gives a list of collection names
    collection = client.get_collection(collection_name)
else:
    print("No embeddings collection found. Please run save_embeddings_into_chroma.py first.")
#print(collection.count())


### 
#loading api key and configuring Gemini API 
### 
from config import api_key #importing api key from config.py 
import google.generativeai as genai 
genai.configure(api_key=api_key) #using api key to authenticate



###
#finally trying to find similar books based on user query
###
def recommend_books(user_query, top_k=5, similarity_threshold=1.0):   #top_k: number of similar books to return 
                                                                    #similarity_threshold: higher number means less similar; 0.0(perfect match) to 1.0(no similarity at all)
    """
     Recommend books based on user query using Gemini embeddings and ChromaDB semantic search filtering by similarity_threshold.
    """

    #generating embedding for user query for semantic search
    embedding_response = genai.embed_content(
        model="models/text-embedding-004",
        content=user_query  #content to embed
    )
    query_embedding = embedding_response['embedding']  #extracting embedding vector


    #searching in chroma db collection for similar embeddings to query embedding
    results = collection.query(     #ChromaDB method that searches the vector database to find similar embeddings
        query_embeddings=[query_embedding],  #comparing user query embedding with stored embeddings to match similar ones
        n_results=top_k,   #number of similar results to return(top 5)
        include=["documents", "distances"] #includes document texts and their ids of top searches
    )

    docs=results["documents"][0]  #extracting document texts of top matches from results
    distances = results["distances"][0] #extracting distances of top matches from results

    #testing
#     print("Distance test:")
#     test = collection.query(
#         query_embeddings=[book_embeddings[0][1]],
#         n_results=3,
#         include=["distances", "documents"]
# )
#     print(test)

    #filtering results by distance threshold 
    recommended = []
    for i in range(len(docs)):
        dist = distances[i]
        if dist <= similarity_threshold:
            recommended.append((docs[i], dist))

    # Sort by distance (closest first)
    for i in range(len(recommended)):
        for j in range(len(recommended) - i - 1):
            if recommended[j][1] > recommended[j + 1][1]:
                recommended[j], recommended[j + 1] = recommended[j + 1], recommended[j]

    #extracting recommended documents from sorted filtered list            
    recommended_books = []
    for item in recommended:
        recommended_books.append(item[0])


    #if none passed the threshold
    if len(recommended_books) == 0:
        return ["Sorry :( We couldn't find any books that match your query in our database. Please try a different query."]

    
    return recommended_books


###
#executing...
###
while True:
    print("write \"exit\" if u do not want any recommendations")
    print("\n")
    query = input("what kind of books do you want to read?")
    recommendations = recommend_books(query) #passes the query and fetches recommended books
    if query.lower() == "exit":
        break
      
    print("---------------------------------------------------------------")
    print("\nthese are some books you might enjoy reading :) \n")
    for result in recommendations:
        print ("-", result,"\n")

    print("happy reading!!!")
    print("-----------------------------------------------------------------")
