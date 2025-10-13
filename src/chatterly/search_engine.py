import wikipedia
from duckduckgo_search import DDGS

def wiki_search(query):
    try:
        return wikipedia.summary(query, sentences=2)
    except Exception:
        return None

def duckduckgo_search(query):
    with DDGS() as ddgs:
        results = ddgs.text(query, max_results=1)
        for r in results:
            return f"{r['title']} - {r['body']} ({r['href']})"
    return "I couldn't find anything relevant."

def search_answer(query):
    wiki = wiki_search(query)
    if wiki:
        return wiki
    return duckduckgo_search(query)
