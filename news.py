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