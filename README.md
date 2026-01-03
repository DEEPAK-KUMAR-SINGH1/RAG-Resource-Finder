📚 AI Resource Finder (RAG + Mistral + Flask)

An AI-powered Resource Finder built using Retrieval-Augmented Generation (RAG) that provides structured answers along with relevant learning resources such as articles, blogs, documentation links, and local PDFs.

🚀 Features

=  RAG-based question answering system
=  Source-grounded AI responses (no hallucinations)
=  Supports URLs + local PDFs
=  Clean and responsive Flask-based UI
=  Topic-wise knowledge base
=  Easily extendable JSON-based data source

🧠 RAG Architecture Explanation
This project follows the Retrieval-Augmented Generation (RAG) architecture, combining semantic search with a large language model.

🔹 Workflow

=  ser Input
=  User enters a topic or question through the Flask web interface.
=  Retrieval
=  All learning resources are stored in resources.json
=  Each resource includes:
=  title
=  url (web link or local PDF)
=  content (semantic description)
=  Text embeddings are generated using a sentence-transformer model
=  FAISS vector search retrieves the most relevant resources

Augmentation
Retrieved resources are compiled into a context block passed to the LLM.

Generation
Mistral LLM generates answers only using retrieved context
If no relevant data is found, the system responds:

"Not found in knowledge base."

Output

Structured AI-generated answer

List of relevant resources with clickable URLs and PDFs

📌 This architecture ensures accuracy, transparency, and reliability.

📂 Data Source Description
🔹 Data Types Used

1)  Online Resources

2)  Research papers (ArXiv)

3)  Official documentation (MDN, AWS, Hugging Face, Node.js)

4)  Educational blogs and guides

5)  Local PDFs

Stored in:

static/pdfs/


Topic-wise PDFs:

1)  AI / Machine Learning
2)  Web Development
3)  Cloud Computing
4)  Cybersecurity
5)  Finance / Healthcare
6)  Knowledge Base File
7)  resources.json

Acts as the single source of truth

PDFs are manually added, not auto-generated

🛠 Tech Stack

1) Frontend
2) HTML
3) Templates
4) Responsive UI
5) Backend
6) Python
7) Flask
8) AI / NLP
9) Mistral LLM (API-based)
10) Sentence-Transformers
11) FAISS (Vector Search)
12) Storage

JSON-based knowledge base

Local static PDF hosting

⚙️ Setup & Run Instructions
🔹 Prerequisites

    Python

Mistral API Key

🔹 Step 1: Create Virtual Environment
    python -m venv myenv
    myenv\Scripts\activate

🔹 Step 2: Install Dependencies in requirements.txt
    flask 
    sentence-transformers 
    faiss-cpu 
    mistralai 
    python-dotenv

🔹 Step 3: Configure Environment Variables

Create a .env file:

MISTRAL_API_KEY=your_mistral_api_key_here

🔹 Step 4: Project Structure
project/
│── app.py
│── resources.json
│── rag/
│   ├── ingest.py
│   ├── embed.py
│   ├── retriever.py
│   └── generator.py
│── templates/
│   └── index.html
│── static/
│   └── pdfs/

🔹 Step 5: Run the Application
python app.py


Open in browser: http://127.0.0.1:5000

⚠️ Limitations

1) PDFs are not parsed internally (only metadata used)

2) Manual updates required for resources.json

3) No authentication or user profiles

4) No resource ranking control

5) Single-language support (English)

🚀 Future Improvements

1) Full PDF text parsing for deep semantic search

2) Topic-wise UI tabs and filters

3) Embedded PDF preview (iframe)

4) Admin panel for uploading resources

5) PDF priority boosting

6) Multi-LLM support (OpenAI, LLaMA, Claude)

7) Cloud deployment (AWS / Azure / Hugging Face Spaces)

✅ Conclusion

This project demonstrates a real-world RAG-based AI system that:

Grounds LLM outputs in trusted sources

Supports both online and offline learning materials

Provides clean, structured, and explainable AI responses

Is scalable, extensible, and portfolio-ready

📌 Ideal for AI internships, academic projects, and production prototypes.


👤 Author

Deepak Kumar Singh
AI Developer intern / Data Science Enthusiast
