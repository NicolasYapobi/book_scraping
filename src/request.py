import requests
import bs4 as BeautifulSoup

def get_request():
    url = "http://books.toscrape.com/"
    response = requests.get(url)
    if response == 200:
        return response
    else:
        print(f"Request error: {response.status_code}")