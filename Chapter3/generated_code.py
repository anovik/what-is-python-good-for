from bs4 import BeautifulSoup
import requests

# URL of page to be scraped
URL = "https://en.wikipedia.org/wiki/Web_scraping"

# sending a get request to the URL
page = requests.get(URL)

# create a BeautifulSoup object from the HTML
soup = BeautifulSoup(page.content, "html.parser")

# extracting all the <p>Tags from the webpage
p_tags = soup.find_all("p")

# go through the paragraphs and print out the text
for p in p_tags:
    print(p.text)
