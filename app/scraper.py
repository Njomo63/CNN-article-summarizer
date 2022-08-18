import requests
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, url):
        page = requests.get(url)
        self.soup = BeautifulSoup(page.content, "html.parser")

    def first(self):
        coverage = self.soup.find_all("p",class_= "zn-body__paragraph speakable")
        return coverage[0].text
    
    def scrape(self):
        first = self.first()
        coverage = self.soup.find_all("div",class_= "zn-body__paragraph")
        for para in coverage:
            first += para.text
        return first