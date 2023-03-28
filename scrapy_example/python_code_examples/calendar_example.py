import requests
from bs4 import BeautifulSoup

url = "https://www.ucm.es/"

response = requests.get(url)
html_content = response.content

# Using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find <a> containing keyword in href
keyword = 'calendario'
links = soup.find_all('a', href=lambda href: href and keyword in href)

# Print URLs
for link in links:
    print(link.get('href'))