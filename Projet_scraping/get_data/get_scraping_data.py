import requests
from bs4 import BeautifulSoup
import pandas as pd

BASE_URL = "http://books.toscrape.com/catalogue/page-{}.html"

def extract_title(book: BeautifulSoup) -> str:
    return book.find("h3").find("a")["title"]

def extract_price(book: BeautifulSoup) -> str:
    return book.find("p", class_="price_color").text

def extract_rating(book: BeautifulSoup) -> str:
    return book.find("p", class_="star-rating")["class"][1]

def extract_availability(book: BeautifulSoup) -> str:
    return book.find("p", class_="instock availability").text.strip()

def extract_book_info(book: BeautifulSoup) -> dict:
    return {
        "title": extract_title(book),
        "price": extract_price(book),
        "rating": extract_rating(book),
        "availability": extract_availability(book)
    }

def scrape_books(nb_books=1000):
    all_books = []
    page = 1
    while len(all_books) < nb_books:
        print(f"Scraping page {page}")
        url = BASE_URL.format(page)
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        books_tags = soup.find_all("article", class_="product_pod")
        if not books_tags:
            print(f"Aucune donnée sur la page {page}. Fin du scraping.")
            break
        books = [extract_book_info(tag) for tag in books_tags]
        all_books.extend(books)
        page += 1

        df = pd.DataFrame(all_books)
    return df

