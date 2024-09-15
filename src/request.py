import requests

def get_request():
    url = "http://books.toscrape.com/"
    return requests.get(url)