from fastapi import FastAPI
from scraper.ecommerce import total_inventory
from scraper.news import total_views

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Web Intelligence Aggregator Running"}

@app.get("/ecommerce/total")
def ecommerce_total():
    return {"total_inventory": total_inventory()}

@app.get("/news/views")
def news_views():
    return {"total_views": total_views()}
