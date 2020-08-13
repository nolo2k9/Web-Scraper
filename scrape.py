import requests
from bs4 import BeautifulSoup

URL = 'https://www.monster.ie/jobs/search/?q=software-developer&where=Galway__2C-Galway&cy=ie&intcid=swoop_HeroSearch_IE'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='ResultsContainer')
job_elems = results.find_all('section', class_='card-content')

for job_elem in job_elems:
    title_elem = job_elem.find('h2', class_='title')
    company_elem = job_elem.find('div', class_='company')
    location_elem = job_elem.find('div', class_='location')
    details_elem = job_elem.find('div', class_='mux-tabs-content')
    if None in (title_elem, company_elem, location_elem):
        continue
    print(title_elem.text.strip())
    print(company_elem.text.strip())
    print(location_elem.text.strip())
    print(details_elem)
    print()
    

