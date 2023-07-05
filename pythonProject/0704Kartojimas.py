
# ------------------KARTOJIMAS(0704)-----------------------------

# 4. Užduotis:
#     [+] Išskirkite informaciją apie produktų kainas ir jų kategorijas iš pigu.lt puslapio naudodami Beautiful Soup
# ir išsaugokite juos į Pandas DataFrame.
#     [+]  Remdamiesi gautais duomenimis sukurkite stulpelinę diagramą,
# kurioje bus pavaizduotos produktų kainos pagal kategorijas mažėjančia tvarka.

import matplotlib.pyplot as plt
# from bs4 import BeautifulSoup
# import pandas as pd
# import time
# import requests
# import re
#
# delay = 2
# url = "https://pigu.lt/lt/"
# response = requests.get(url)
#
# #tikriname ar uzklausa buvo sekminga
# if response.status_code == 200:
#     content = response.content
#     # print("status code: " + str(response.status_code))
#     soup = BeautifulSoup(response.content, 'html.parser')
#     category_links = soup.find_all('a', class_='departament-link')
#
#
#     categories = []
#     prices = []
#     products = []
#     counter = 0
#     # imant daugybe duomenu jis reikalingas kad neskaiciuotu visu duomenu, siuo atveju 3Mil produktu
#     for link in category_links:
#         category_url = link['href']
#         category_name = link.text.strip()
#
#         category_response = requests.get(category_url)
#         category_content = category_response.content
#         category_soup = BeautifulSoup(category_content, 'html.parser')
#         product_name = category_soup.find_all('p', class_='product-name')
#         product_price = category_soup.find_all('div', class_='product-price')
#     #apsirasyti for kuris eis per kainas ir prides i lista su kategorjomis
#         for price, name in zip (product_price, product_name):
#             #pasaliname nereikalingus text kuris yra salia kainos
#             numeric_price = re.sub('[^0-9]', '', price.text.strip())
#             prices.append(numeric_price)
#             categories.append(category_name)
#             products.append(name.text.strip)
#             counter += 1
#             if counter == 1000:
#                 break
#         if counter == 1000:
#             break
# df = pd.DataFrame({
#     'kategorija': categories,
#     'pavadinimas': products,
#     'kaina': prices,
#     })
#
# df['kaina'] = pd.to_numeric(df['kaina'])
# print(df)
#
# df_sorted = df.sort_values(by='kaina', ascending=False)
#
# print(df_sorted)





