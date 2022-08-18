# import requests
# from bs4 import BeautifulSoup
from app.scraper import Scraper
from transformers import pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
    
@app.post("/summarise")
def summarize_article(article_url):
    article = Scraper(article_url)
    ARTICLE = article.scrape()
    if len(ARTICLE) < 1024:
        return summarizer(ARTICLE, max_length=300, min_length=130, do_sample=False)
    return summarizer(ARTICLE[:1024], max_length=300, min_length=130, do_sample=False)