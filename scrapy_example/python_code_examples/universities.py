import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import urljoin

# Spanish universities
universidades = [
    "https://www.uab.es/",
    "https://www.uam.es",
    "https://www.uc3m.es/",
    "https://www.ucm.es/",
    "https://www.udc.es/",
    "https://www.uah.es/",
    "https://www.ua.es/",
    "https://www.ual.es/",
    "https://www.ub.edu/",
    "https://www.ubu.es/",
    "https://www.uca.es/",
    "https://www.unican.es/",
    "https://www.uclm.es/",
    "https://www.uco.es/",
    "https://www.unex.es/",
    "https://www.udg.edu/",
    "https://www.ugr.es/",
    "https://www.uhu.es/",
    "https://www.ujaen.es/",
    "https://www.ull.es/",
    "https://www.unirioja.es/",
    "https://www.ulpgc.es/",
    "https://www.unileon.es/",
    "https://www.udl.es/",
    "https://www.uma.es/",
    "https://www.um.es/",
    "https://www.uniovi.es/",
    "https://www.usal.es/",
    "https://www.usc.es/",
    "https://www.us.es/",
    "https://www.uva.es/",
    "https://www.uvigo.es/",
    "https://www.unizar.es/",
    "https://www.ehu.es/",
    "https://www.unia.es/",
    "https://www.uimp.es/",
    "https://www.umh.es/",
    "https://www.uned.es/",
    "https://www.upo.es/",
    "https://www.upct.es/",
    "https://www.upc.es/",
    "https://www.upm.es/",
    "https://www.upv.es/",
    "https://www.upf.edu/es/",
    "https://www.unavarra.es/",
    "https://www.urjc.es/",
    "https://www.urv.es/",
    "https://www.uib.es/",
    "https://www.uv.es/",
    "https://www.uji.es/",
]

# Find <a> containing keyword in href
keyword = 'calendario'

results = []

def get_university_async(url):
    response = requests.get(url)
    html_content = response.content
    soup = BeautifulSoup(html_content, 'html.parser')
    links = soup.find_all('a', href=lambda href: href and keyword in href)
    return [link.get('href') for link in links]

with ThreadPoolExecutor() as executor:
    futures = [executor.submit(get_university_async, url) for url in universidades]
    for future in as_completed(futures):
        results += future.result()

# Print URLs
for link in results:
    print(link)