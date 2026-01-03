from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# embedding model 
model = SentenceTransformer("all-MiniLM-L6-v2")

def create_vector_store(docs):
    embeddings = model.encode(
        [d["text"] for d in docs],
        show_progress_bar=True
    )

    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(np.array(embeddings))

    return index, docs
