import requests
from bs4 import BeautifulSoup

url = "https://www.otago.ac.nz/courses/qualifications/ba.html"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    divs = soup.find_all('div', class_='requirements-panel__container')
    print(divs)
    if divs and len(divs) > 1:
        # Exclude the first div and find the table in each of the other divs
        for i in range(1, len(divs)):
            major_table = divs[i].find('table')

            if major_table:
                print(f"Found table in div {i}")
            else:
                print(f"No table found in div {i}")
    else:
        print("No suitable divs found.")
else:
    print(f"Failed to retrieve content. HTTP Status code: {response.status_code}")

