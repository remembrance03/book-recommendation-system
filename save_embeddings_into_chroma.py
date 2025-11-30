import chromadb
#from generating_embeddings import embeddings, book_texts  

#to import embeddings saved as a pickle file(locally); doesnt run generating_embeddings.py again and again :)
import pickle
#loading saved embeddings and texts
with open("embeddings.pkl", "rb") as f:
    saved_data = pickle.load(f)

vector = [emb[1] for emb in saved_data["embeddings"]]  #extracting only the vectors  
book_texts = book_texts = [text for (_, text) in saved_data["titles"]]    #only the string text from (id, text) tuples


client = chromadb.PersistentClient(path="chroma_db") #creating a persistent client that saves the vector database to a folder named chroma_db (if db doesnt exists)
                                                    #persistentClient ensures your vector database is saved and can be reopened later

collection = client.get_or_create_collection(name="books") #creates collection named books and if already exists it retrieves it



storing=collection.add(
        ids=[str(i) for i in range(len(book_texts))],  ##chroma requires string ids so converting ids to string
        documents=book_texts,   #getting the combined text for the book id and appends the text whose id matches book_id
        embeddings=vector #list of embedding vectors
)


print("stored embeddings in ChromaDB!!!")
