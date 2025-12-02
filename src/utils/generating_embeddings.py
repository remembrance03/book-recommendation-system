####
#generating embeddings for the prepared book texts
###
from openai import embeddings
from src.core.config import settings  #importing settings instance from config.py
import google.generativeai as genai
from src.utils.prepare_books import load_books_for_embedding


genai.configure(api_key=settings.api_key)  #using api key to authenticate


book_texts = load_books_for_embedding()  #loading prepared book texts


def generate_embeddings():
    embeddings = []  #empty list to store embeddings
    for id_, text in book_texts:
        #emb contains the embedding vector inside like this... emb['embedding']
        emb = genai.embed_content(   #calling gemini api to generate embeddings
            model="models/text-embedding-004",  #embedding model
            content=text 
        )
        embeddings.append((id_, emb['embedding']))  #storing id and embedding vector as tuple in list
        
    print("\ngenerated embeddings for all books!\n")
    return embeddings


###
#saving in pickle files for later use(locally)
###
def save_embeddings(embeddings):
    import pickle
    from src.core.config import settings

    #saving both in a dictionary format instead of list of tuples for easier access later
    data_to_save = {
        "titles": book_texts,
        "embeddings": embeddings
    }

    #finally saving to pickle
    from src.utils.save_picklefile import save_embeddings
    save_embeddings(data_to_save)

    print("Embeddings and titles saved successfully!")
    print("----------------------------------------------------")
    print("\nSaved embeddings and book texts as pickle files!")


#for user query embedding generation
def generate_User_embeddings(user_query: str):
    #generating embedding for user query for semantic search
    embedding_response = genai.embed_content(
        model="models/text-embedding-004",
        content=user_query  #content to embed
    )
    query_embedding = embedding_response['embedding']  #extracting embedding vector
    return query_embedding 
