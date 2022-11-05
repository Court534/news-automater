import requests
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
    return response.json()["articles"]

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
    query_params = {
        "category": category,
        "country": "gb",
        "apiKey": API_KEY 
    }
    
    response = requests.get(URL, params=query_params)
    sources = response.json()["sources"]
    
    for source in sources:
        print(source["name"])
        print(source["url"])
        
        
