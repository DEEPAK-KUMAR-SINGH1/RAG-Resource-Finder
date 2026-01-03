from mistralai import Mistral
import os

client = Mistral(api_key=os.getenv("MISTRAL_API_KEY"))

def generate_answer(query, context_docs):
    context = "\n".join([d["text"] for d in context_docs])

    prompt = f"""
You are a precise and helpful AI assistant.

Answer the QUESTION using **only** the information provided in the SOURCES below.
You may summarize or rephrase the content, but you must NOT use any external knowledge or assumptions.

If the answer cannot be derived from the SOURCES, respond **exactly** with:
"Not found in knowledge base."

Answer format requirements:
1. Begin with a short definition (3–4 concise lines).
   - Do NOT include a heading for the definition.
2. After the definition, list **2–4 key components**.
   - Use clear and meaningful headings for each component.
3. Keep the response well-structured and easy to read.
4. Use short paragraphs or bullet points where appropriate.
5. Maintain a professional, neutral, and informative tone.
6. Do NOT mention the sources explicitly in the final answer.
7. also in "Sources Used" section show first related pdf of the content. 

SOURCES:
{context}

QUESTION:
{query}

FINAL ANSWER:
"""


    response = client.chat.complete(
        model="mistral-small",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content
