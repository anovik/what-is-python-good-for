import requests
from bs4 import BeautifulSoup

response = requests.get(
	url="https://en.wikipedia.org/wiki/Python_(programming_language)",
)
soup = BeautifulSoup(response.content, 'html.parser')

title = soup.find(id="firstHeading")
print(title.text)

print()

# Get all the links
allLinks = soup.find(id="bodyContent").find_all("a")

[print(link.get('href')) for link in allLinks[:10]]
    
print()
    
#Get the first link
firstLink = soup.select_one("#bodyContent a")
print(firstLink.get('href'))

print()

#Get the link number...
anotherLink = soup.select("#bodyContent a")[20]
print(anotherLink.get('href'))

print()

#Get section titles
sections = soup.find_all("span", class_="mw-headline")
[print(section.text) for section in sections]

