import requests
from bs4 import BeautifulSoup

response = requests.get(
	url="https://en.wikipedia.org/wiki/Python_(programming_language)",
)
soup = BeautifulSoup(response.content, 'html.parser')

title = soup.find(id="firstHeading")
print(title.text)

# Get all the links
allLinks = soup.find(id="bodyContent").find_all("a")

#for link in allLinks:
	#print(link)
    
#Get the first link

#Get the next link

#Get the previous link

#Get section titles

