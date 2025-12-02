###optional
#For generating embeddings and book_texts everysingle time we run this file, we would have to run generating_embeddings.py
#from generating_embeddings import embeddings, book_texts  
###

#to import embeddings saved as a pickle file(locally); doesnt run generating_embeddings.py again and again :)
import pickle
from src.core.config import settings #for getting EMBEDDINGS_FILE path

#loading saved embeddings and texts
from src.utils.open_picklefile import load_pickle
saved_data = load_pickle()

#extracting embeddings and book_texts from the loaded pickle data
vector = [emb[1] for emb in saved_data["embeddings"]]  #extracting only the vectors  
book_texts = book_texts = [text for (_, text) in saved_data["titles"]]    #only the string text from (id, text) tuples


#chromadb client connection and collection creation
from src.core.chromadb_connection import get_collection 


collection = get_collection("books")  #creates collection named books and if already exists it retrieves it


storing=collection.add(
        ids=[str(i) for i in range(len(book_texts))],  ##chroma requires string ids so converting ids to string
        documents=book_texts,   #getting the combined text for the book id and appends the text whose id matches book_id
        embeddings=vector #list of embedding vectors
)


print("stored embeddings in ChromaDB!!!")
