import chromadb
#from generating_embeddings import embeddings, book_texts  

#to import embeddings saved as a pickle file(locally); doesnt run generating_embeddings.py again and again :)
import pickle
#loading saved embeddings and texts
with open("embeddings.pkl", "rb") as f:
    saved_data = pickle.load(f)

embeddings = saved_data["embeddings"]   # list of embedding vectors
book_texts = saved_data["titles"]       # list of combined book texts


client = chromadb.PersistentClient(path="chroma_db") #creating a persistent client that saves the vector database to a folder named chroma_db (if db doesnt exists)
                                                    #persistentClient ensures your vector database is saved and can be reopened later

collection = client.get_or_create_collection(name="books") #creates collection named books and if already exists it retrieves it


#prepare data dictionar
data = {
    "ids": [],
    "documents": [],
    "embeddings": []
}

collection.add(
     ids=[str(i) for i in range(len(book_texts))],  ##chroma requires string ids so converting ids to string
    documents=book_texts,  # #getting the combined text for the book id and appends the text whose id matches book_id
    embeddings=embeddings
)


print("stored embeddings in ChromaDB!!!")
