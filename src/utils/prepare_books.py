####
#preparing text for embedding 
###
from src.core.db_connection import get_connection


def load_books_for_embedding():
    """
    Loads all books from the database and prepares the text for embeddings.
    Returns a list of tuples: (id, prepared_text)
    """
    conn = get_connection()
    cursor = conn.cursor()
    #reading all the data from the books table
    cursor.execute("SELECT id, title, genre, author, summary FROM books")
    rows = cursor.fetchall()

    conn.close()

    #prints all data fetched from the database(testing)
    #printing data row by row
    # for row in rows:
    #     print(row)
        

    # Prepare text for embeddings
    book_texts = []    #this list will store all the books in a format ready for embeddings
    for (id_, title, genre, author, summary) in rows:           #id is already a built-in Python so using id_ instead
        text = f"{title} by {author}. Genre: {genre}. Summary: {summary}"
        book_texts.append((id_, text))   #stores in format of id and combined text of title, author, genre, summary


    #checking prepared text
    # print("--------------------------------")
    # print("\n PREPARED TEXT:\n")
    # for id_, text in book_texts:
    #     print(id_, text)
    # print("--------------------------------")




###
#preparing embeddings for recommendation system
###
from src.core.config import settings #for getting EMBEDDINGS_FILE path

def load_embeddings():
    ###
    #loadinggg... files
    ###

    from src.utils.open_picklefile import load_pickle
    saved_data = load_pickle()

    vector = [emb[1] for emb in saved_data["embeddings"]]  #extracting only the vectors  
    book_texts = [text for (_, text) in saved_data["titles"]]    #only the string text from (id, text) tuples

    print("loaded embeddings for", len(book_texts), "books.") 
    return vector, book_texts

    #testing
    # print(type(book_embeddings[0]))
    # print(book_embeddings[0])
