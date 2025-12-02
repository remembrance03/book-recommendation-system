import os
from pathlib import Path  #for handling file paths
from dotenv import load_dotenv   #for loading environment variables
from functools import lru_cache #for caching settings instance

# Get the project root directory
PROJECT_ROOT = Path(__file__).parent.parent.parent  

# Load environment variables
load_dotenv(PROJECT_ROOT / ".env")

@lru_cache()
class Settings:
    #project paths
    PROJECT_ROOT: Path = PROJECT_ROOT
    SRC_DIR: Path = PROJECT_ROOT / "src"  #source code directory
    DATA_DIR: Path = PROJECT_ROOT / "data"  #data directory
    SERVICES_DIR: Path = SRC_DIR / "services"  #services directory
    CORE_DIR: Path = SRC_DIR / "core"  #core directory


    #SQLite database path
    DB_PATH: Path = PROJECT_ROOT / "data" / "books.db"

    #CSV file path
    csv_file_path : Path = PROJECT_ROOT / "data" / "books.csv"


    #embeddings pickle file path
    EMBEDDINGS_FILE: Path = PROJECT_ROOT / "data" / "embeddings.pkl"

    #API key configuration
    api_key: str | None = os.getenv("GOOGLE_API_KEY") 
    

    #model configuration
    EMBEDDING_MODEL = "models/text-embedding-004"
    GENERATION_MODEL = "models/gemini-1.5-flash"
    SUMMARY_MODEL = "models/gemini-1.5-flash-8b"

    

# Create a singleton instance
settings = Settings()