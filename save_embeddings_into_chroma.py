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

for book_id, emb in embeddings:
    data["ids"].append(str(book_id))  ##chroma requires string ids so converting ids to string
    text = next(text for i, text in book_texts if i == book_id)  # #getting the combined text for the book id and appends the text whose id matches book_id
    data["documents"].append(text) #appending combined text for the book
    data["embeddings"].append(emb) #appending embedding vector for the book


#inserting into chroma collection all at once
collection.add(
    ids=data["ids"],
    embeddings=data["embeddings"],
    documents=data["documents"] 
)

print("stored embeddings in ChromaDB!!!")
