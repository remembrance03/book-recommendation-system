import pickle
from src.core.config import settings

def load_pickle():
    """
    Load the pickle file from EMBEDDINGS_FILE path.
    Returns:data: The raw data stored in the pickle file
    """
    embeddings_file = settings.EMBEDDINGS_FILE

    with open(embeddings_file, "rb") as f:
        data = pickle.load(f)

    print(f"Loaded data from {embeddings_file}")
    return data