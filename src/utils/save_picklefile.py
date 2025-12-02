import pickle
from src.core.config import settings

def save_embeddings(data_to_save: dict):
    """
    Save embeddings (or any data) to the pickle file.
    """
    embeddings_file = settings.EMBEDDINGS_FILE
    with open(embeddings_file, "wb") as f:
        pickle.dump(data_to_save, f)

    print(f"Saved data to {embeddings_file}")








