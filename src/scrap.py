from request import *
import bs4 as BeautifulSoup


def scrap():
    response = get_request()
    print(response)
    if response.status_code == 200:
        soup = BeautifulSoup.BeautifulSoup(response.content, "html.parser")
        books = soup.find_all('article', class_='product_pod')
        for book in books:
            title = book.h3.a['title']
            print(title)
    else:
        print("Request error: {response.status_code}")
