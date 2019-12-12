"""
This is the main file for the program
It receives the html file and prints data
Order of files in this project app.py > page.py > BookParser.py > locators.py
"""


import requests
from page.py import Page

while True:
    # print from page
    page = input('Get books from page: ')

    url = f'http://books.toscrape.com/catalogue/page-{page}.html'
    html = requests.get(url).content

    # Page makes the BeautifulSoup
    books = Page(html)
    # .books is a method that returns a list of objects, each being information about the book
    all_books = books.books()

    # converts rating from string to integer
    rating_dict = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}

    # print all of the books' data
    for book in all_books:
        print(f'Book: {book.get_book()}')
        print(f'Rating: {rating_dict[book.get_rating()]}')
        print(f'Price: £{book.get_price()}\n')
