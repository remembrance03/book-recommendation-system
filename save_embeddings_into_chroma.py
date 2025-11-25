import chromadb
#from generating_embeddings import embeddings, book_texts  

#to import embeddings saved as a pickle file(locally); doesnt run generating_embeddings.py again and again :)
import pickle
#loading saved embeddings and texts
with open("embeddings.pkl", "rb") as f:
    embeddings = pickle.load(f)

with open("book_texts.pkl", "rb") as f:
    book_texts = pickle.load(f)


client = chromadb.PersistentClient(path="chroma_db") #creating a persistent client that saves the vector database to a folder named chroma_db
                                                    #persistentClient ensures your vector database is saved and can be reopened later

collection = client.get_or_create_collection(name="books") #creates collection named books and if already exists it retrieves it


#embeddings=(id_, embedding_vector)

ids = []  #book ids
texts = []  #combined text of title, author, genre, summary
vectors = []   #embedding vector for each book


for book_id, emb in embeddings:
    ids.append(str(book_id))     #chroma requires string ids so converting ids to string
    texts.append(next(text for i, text in book_texts if i == book_id))   #getting the combined text for the book id and appends the text whose id matches book_id
    vectors.append(emb)   #appending embedding vector for the book

#inserting into chroma collection all at once
collection.add(
    ids=ids,
    embeddings=vectors,
    documents=texts
)

print("stored embeddings in ChromaDB!!!")
