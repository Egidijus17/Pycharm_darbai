

# -----------------------------KARTOJIMAS(07.07)----------------------------------

# -------Automatinis duomenu surinkimas is keliu website----------------

import pandas as pd
import requests
from bs4 import BeautifulSoup

def scrap_job_listings():
    job_listings = []
    # urls = ['https://www.cvbankas.lt/', 'https://www.cv.lt/']
    websites = [{
        'url': 'https://www.cvbankas.lt/',
        'job_listening_selector': 'div#js_id_id_job_ad_list',
        'title': 'h3.list_h3',
        'company': 'span.heading_secondary',
        'location': 'span.list_city',
        'salary': 'span.salary_amount'
        },
        {'url': 'https://www.cv.lt/',
        'job_listening_selector': 'main.col-xs-12.col-12.col-lg.main-content',
        'title': 'button.title',
        'company': 'span.company',
        'location': 'div.row:nth-child(4) > div:nth-child(1) > div:nth-child(1) > a:nth-child(1) > '
                    'div:nth-child(3) > span:nth-child(2) > span:nth-child(2)',
        'salary': 'span.salary'
        }
    ]

    for website in websites:
        url = website['url']
        response = requests.get(url)

        soup = BeautifulSoup(response.text, 'html.parser')
        job_elements = soup.select(website['job_listening_selector'])
        for job_element in job_elements:
            title = job_element.select_one(website['title']).text.strip()
            company = job_element.select_one(website['company']).text.strip()
            location = job_element.select_one(website['location']).text.strip()
            salary = job_element.select_one(website['salary']).text.strip()
            job_listings.append({
                'Title': title,
                'Company': company,
                'Location': location,
                'Salary': salary
            })

    return job_listings

job_listings = scrap_job_listings()

data = pd.DataFrame(job_listings)
print(data)
