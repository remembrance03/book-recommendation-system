# The LibQuery

This repository contains the source code for a book recommendation system developed in Python. The goal of this project is to provide personalized book suggestions to users based on their input (e.g., a book title or reading preference). 

The system uses an embedding-based semantic similarity approach, where book descriptions are converted into high-dimensional vectors using Gemini embedding models. User queries are embedded in the same vector space, and ChromaDB performs vector similarity search using distance metrics to retrieve the most semantically similar books.

---

## Features

- Provides personalized book recommendations based on user queries
- Uses semantic embeddings for high-quality similarity matching
- Supports configurable similarity thresholds and top-k recommendations
- Modular Python code structure for easy extension or integration

---

## Installation and Execution

1. Clone the repository
   
   ```
   git clone https://github.com/remembrance03/book-recommendation-system.git
   cd book-recommendation-system
   ```
2. Install dependencies
   
   ```
   pip install -r requirements.txt
   ```
3. Ensure book embeddings are generated and saved into ChromaDB
   
   ```
   python src/utils/save_embeddings_into_chroma.py
   ```
4. Start the recommendation system
   
   ```
   python src/main.py
   ```
5. Enter a book title or your reading preferences. The system will match your query with the books that are similar in the database and return the recommended books sorted by similarity

---

## How It Works

1. **Load Book Embeddings:** Pre-generated embeddings of book descriptions are loaded from ChromaDB
2. **User Query Embedding:** The input query is converted into a high-dimensional embedding using the Gemini embedding model
3. **Vector Similarity Search:** ChromaDB compares the query embedding with stored book embeddings
4. **Filtering & Sorting:** Books with distances below a user-defined similarity threshold are returned sorted by closeness
5. **Recommendations:** The top-k most similar books are presented as recommendations   
