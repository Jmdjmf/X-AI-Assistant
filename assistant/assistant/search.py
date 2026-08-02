from googlesearch import search

def web_search(query):
    try:
        results = []
        for url in search(query, num_results=5):
            results.append(url)
        return results
    except Exception:
        return []
