import requests
from bs4 import BeautifulSoup

artist_id = "3OKg7YbOIatODzkRIbLJR4"

soup = BeautifulSoup(
    requests.get("https://open.spotify.com/artist/" + artist_id).content, "html.parser"
)

if "BdOdd" in soup.text:
    print(soup.prettify())


cities = soup.find_all(class_="BdOdd")

for city in cities:
    print(city.text)

# <div data-encore-id="type" class="Type__TypeElement-sc-goli3j-0 BdOdd">Mumbai, IN</div>
