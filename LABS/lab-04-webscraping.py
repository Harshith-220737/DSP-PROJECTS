import requests
from bs4 import BeautifulSoup

# website url
url = "https://webscraper.io/test-sites/e-commerce/allinone/computers"

# send request
response = requests.get(url)

# check status
if response.status_code != 200:
    print("page not loaded")
    exit()

# parse html
soup = BeautifulSoup(response.text, "html.parser")

products = []

# get each product card
cards = soup.find_all("div", class_="product-wrapper")

for card in cards:
    title = card.find("a", class_="title").text.strip()
    description = card.find("p", class_="description").text.strip()
    price = card.find("h4", class_="price").text.strip()
    rating = len(card.find("div", class_="ratings").find_all("span", class_="ws-icon-star"))
    reviews = card.find("p", class_="review-count").text.split(" ")[0]

    products.append({
        "title": title,
        "description": description,
        "price": price,
        "rating": rating,
        "reviews": reviews
    })

# print result
for p in products:
    print(p)