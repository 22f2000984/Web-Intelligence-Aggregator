from bs4 import BeautifulSoup

def total_views():
    with open("data/sample.html") as f:
        soup = BeautifulSoup(f, "html.parser")

    total = 0
    for article in soup.select(".article"):
        total += int(article["data-views"])

    return total
