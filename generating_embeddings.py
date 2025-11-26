###
#reading data from the books database 
###
import sqlite3

#connecting
conn = sqlite3.connect("books.db")
cursor = conn.cursor()

#reading all the data from the books table
cursor.execute("SELECT id, title, genre, author, summary FROM books")
rows = cursor.fetchall()

conn.close()

#printing data row by row
for row in rows:
    print(row)



####
#preparing text for embedding 
###
book_texts = []    #this list will store all the books in a format ready for embeddings
for (id_, title, genre, author, summary) in rows:           #id is already a built-in Python so using id_ instead
    text = f"{title} by {author}. Genre: {genre}. Summary: {summary}"
    book_texts.append((id_, text))   #stores in format of id and combined text of title, author, genre, summary

#checking prepared text
print("--------------------------------")
print("\n PREPARED TEXT:\n")
for id_, text in book_texts:
    print(id_, text)
print("--------------------------------")



####
#generating embeddings for the prepared book texts
###
from config import api_key #importing api key from config.py
import google.generativeai as genai

genai.configure(api_key=api_key)  #using api key to authenticate

embeddings = []  #empty list to store embeddings
for id_, text in book_texts:
    #emb contains the embedding vector inside like this... emb['embedding']
    emb = genai.embed_content(   #calling gemini api to generate embeddings
        model="models/text-embedding-004",  #embedding model
        content=text 
    )
    embeddings.append((id_, emb['embedding']))  #storing id and embedding vector as tuple in list

print("\ngenerated embeddings for all books!\n")




###
#saving in pickle files for later use(locally)
###
import pickle

#saving both in a dictionary format instead of list of tuples for easier access later
data_to_save = {
    "titles": book_texts,
    "embeddings": embeddings
}

#finally saving to pickle
with open("embeddings.pkl", "wb") as f:
    pickle.dump(data_to_save, f)

print("Embeddings and titles saved successfully!")
print("----------------------------------------------------")
print("\nSaved embeddings and book texts as pickle files!")


