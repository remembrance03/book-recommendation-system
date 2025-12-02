import chromadb
from openai import _client
from src.core.config import settings

client = None
#create a persistent client
def get_chromadb_connection():
    global client
    if client is None:
        client = chromadb.PersistentClient(path=settings.CHROMA_PATH) 
        #creating a persistent client that saves the vector database to a db in the specified path (if db doesnt exists)
        #persistentClient ensures your vector database is saved and can be reopened later
        return client


def get_collection(name: str):
    """
    Get an existing collection or create a new one.
    """
    if client is None:
        get_chromadb_connection()
    return client.get_or_create_collection(name=name) 
#returns the collection object, which is used to:
#add documents (collection.add(...))
#query embeddings (collection.query(...))
#update or delete entries