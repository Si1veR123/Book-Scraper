"""
This file makes the BeautifulSoup and selects each of the books
"""


from bs4 import BeautifulSoup
from Web_Scraping.Web_Scraper_Books.Parsers.BookParser import Parser
from Web_Scraping.Web_Scraper_Books.Locators.locators import Locators

class Page:
    def __init__(self, html):
        # make the BeautifulSoup
        self.s = BeautifulSoup(html, 'html.parser')

    def books(self):
        # gets each of the books and passes it to BookParser, to extract data. Then returns the BookParser object
        return [Parser(b) for b in self.s.select(Locators.book)]