import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.papergrad.com/")
print(page)

soup = BeautifulSoup(page.content, 'html.parser')
print(soup.prettify())

any_tag = soup.find('a')
print(any_tag.get_text())

multi_tag = soup.find_all('a')
print("Total 'a' tags on our page:",len(a_tag))
for tag in multi_tag :
    print(tag.get_text())
