import json

def load_documents(path="data/resources.json"):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    docs = []
    for item in data:
        text = item["content"]
        for i in range(0, len(text), 300):
            docs.append({
                "text": text[i:i+300],
                "title": item["title"],
                "url": item["url"]
            })
    return docs
