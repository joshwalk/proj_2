import requests
from bs4 import BeautifulSoup

url = 'https://www.si.umich.edu/directory?field_person_firstname_value=&field_person_lastname_value=&rid=All'

count = 1
name_list = []
title_list = []
while count <= 12:
    r = requests.get(url, headers={'User-Agent': 'SI_CLASS'})
    soup = BeautifulSoup(r.text, "lxml")

    name_div = soup.find_all("div", {"property" : "dc:title"})
    for names in name_div:
        name_list.append(names.h2.text)

    title_div = soup.find_all("div", {"class" : "field-name-field-person-titles"})
    for titles in title_div:
        title_list.append(titles.div.div.text)

    count += 1
    url = "https://www.si.umich.edu/directory?field_person_firstname_value=&field_person_lastname_value=&rid=All&page=" + str(count)

contact_dict = dict(zip(name_list,title_list))
print(contact_dict)

# headline_list = []
# most_read_div = soup.find(class_="view-most-read")
# links = most_read_div.find_all('a')
# for link in links:
#     headline_list.append(link.text.strip())
#
# print(headline_list)
