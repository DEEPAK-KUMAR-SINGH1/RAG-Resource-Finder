def retrieve(query, index, docs, model, k=5):
    q_embedding = model.encode([query])
    distances, indices = index.search(q_embedding, k)

    seen = set()
    results = []

    for i in indices[0]:
        key = (docs[i]["title"], docs[i]["url"])
        if key not in seen:
            seen.add(key)
            results.append(docs[i])

    return results
