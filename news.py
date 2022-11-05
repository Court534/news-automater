import requests
from sys import argv
import creds

URL = "https://newsapi.org/v2/top-headlines?"
API_KEY = creds.API_KEY

def get_articles_by_category(category):
    query_params = {
        "category": category,
        "country": "gb",
        "sortBy": "top",
        "apiKey": API_KEY 
    }
    return _get_articles(query_params)

def get_articles_by_query(query):
    query_params = {
        "q": query,
        "sortBy": "top",
        "country": "gb",
        "apiKey": API_KEY 
    }
    return _get_articles(query_params)

def _get_articles(params):
    response = requests.get(URL, params=params)
    articles = response.json()["articles"]

    results = []
    
    for article in articles:
        results.append({
            "title": article["title"],
            "url": article["url"]
        })
        
    for result in results:
        print(result["title"])
        print(result["url"])
        print("")
        
def get_sources_by_category(category):
    url = "https://newsapi.org/v2/top-headlines/sources"
    query_params = {
        "category": category,
        "language": "en",
        "apiKey": API_KEY 
    }
    
    response = requests.get(URL, params=query_params)
    sources = response.json()["sources"]
    
    for source in sources:
        print(source["name"])
        print(source["url"])
        
if __name__ == "__main__":
    print(f"Getting news for {argv[1]}...\n")
    get_articles_by_category(argv[1])
    print(f"Successfully retrieved top {argv[1]} headlines")
        
        
