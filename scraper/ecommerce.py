from bs4 import BeautifulSoup

def total_inventory():
    with open("data/sample.html") as f:
        soup = BeautifulSoup(f, "html.parser")

    total = 0
    for item in soup.select(".product"):
        price = float(item["data-price"])
        stock = int(item["data-stock"])
        total += price * stock

    return round(total, 2)
