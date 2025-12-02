###
#loadinggg... files
###
from src.utils.prepare_books import load_embeddings

book_embeddings, book_texts = load_embeddings() #loading saved embeddings and texts 


###
#connectinggg... chroma_db
###
from src.core.config import settings  #importing settings instance from config.py
from src.core.chromadb_connection import get_collection

collection_name = "books"  #collection that stores book embeddings from save_embeddings_into_chroma.py
#if collection exists then load it
collection = get_collection(collection_name) 
if collection is None:
    print("No embeddings collection found. Please run save_embeddings_into_chroma.py first.")
#print(collection.count())



###
#finally trying to find similar books based on user query
###
def recommend_books(user_query, top_k=10, similarity_threshold=1.0):   #top_k: number of similar books to return 
                                                                    #similarity_threshold: higher number means less similar; 0.0(perfect match) to 1.0(no similarity at all)
    """
     Recommend books based on user query using Gemini embeddings and ChromaDB semantic search filtering by similarity_threshold.
    """

    #generating embedding for user query for semantic search
    from src.utils.generating_embeddings import generate_User_embeddings
    query_embedding = generate_User_embeddings(user_query)


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

    # Sort by distance (closest first) using basic loops
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
