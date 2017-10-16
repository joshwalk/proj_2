import requests
from bs4 import BeautifulSoup

base_url = 'http://www.michigandaily.com'
r = requests.get(base_url)
soup = BeautifulSoup(r.text, "lxml")

headline_list = []
most_read_div = soup.find(class_="view-most-read")
links = most_read_div.find_all('a')
for link in links:
    headline_list.append(link.text.strip())

print(headline_list)
