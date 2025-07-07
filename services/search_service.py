
import json
import os

DATA_PATH = os.path.join(os.path.dirname(__file__), "../data/un_cybercrime_ontology_en.json")

with open(DATA_PATH, "r", encoding="utf-8") as f:
    articles = json.load(f)

def search_articles(query):
    results = []
    query_lower = query.lower()
    for article in articles:
        text_blob = " ".join([str(article.get(k, "")).lower() for k in [
            "Article Title", "Full Text", "Legal Interpretation", "Keywords"
        ]])
        if query_lower in text_blob:
            results.append({
                "Article ID": article["Article ID"],
                "Article Title": article["Article Title"],
                "Snippet": article["Full Text"][:300] + "..."
            })
    return results
