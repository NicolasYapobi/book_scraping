from request import *
import mysql.connector
import bs4 as BeautifulSoup


def start_my_db():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="library"
    )
    return db

def insert_into_db(db, title, price, availability):
    cursor = db.cursor()
    sql = "INSERT INTO books (title, price, availability) VALUES (%s, %s, %s)"
    val = (title, price, availability)
    cursor.execute(sql, val)
    db.commit()

def scrap():
    response = get_request()
    print(response)
    if response.status_code == 200:

        database = start_my_db()
        soup = BeautifulSoup.BeautifulSoup(response.content, "html.parser")
        books = soup.find_all('article', class_='product_pod')
        for book in books:
            title = book.h3.a['title']
            price = book.find('p', class_='price_color').text[1:]
            availability = book.find('p', class_='instock availability').text.strip()
            insert_into_db(database, title, price, availability)
            print(f"{title}, {price}, {availability} inserted")
    else:
        print("Request error: {response.status_code}")
