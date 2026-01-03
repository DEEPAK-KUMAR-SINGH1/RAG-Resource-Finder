from flask import Flask, render_template, request
from rag.ingest import load_documents
from rag.embed import create_vector_store, model
from rag.retriever import retrieve
from rag.generator import generate_answer

app = Flask(__name__)

# Load & index documents ONCE at startup
docs = load_documents()
index, docs = create_vector_store(docs)

@app.route("/", methods=["GET", "POST"])
def home():
    answer = None
    retrieved = []

    if request.method == "POST":
        query = request.form.get("query")

        if query:
            retrieved = retrieve(query, index, docs, model)
            answer = generate_answer(query, retrieved)

    return render_template(
        "index.html",
        answer=answer,
        retrieved=retrieved
    )

if __name__ == "__main__":
    app.run(debug=True)
