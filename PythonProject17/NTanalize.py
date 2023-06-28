# URL: https://en.aruodas.lt/gyvenamieji-namai/
# Nuskenuokite nekilnojamojo turto skelbimus iš nekilnojamojo turto svetainės naudodami BeautifulSoup biblioteką.
# Išskirkite nekilnojamojo turto duomenis, įskaitant kainą, vietą, miegamųjų kambarių skaičių.
# Įrašykite duomenis į Pandas DataFrame ir juos analizuokite,
# siekiant nustatyti tendencijas nekilnojamojo turto rinkoje,
# pavyzdžiui, vidutines kainas skirtingose vietovėse ar populiarius nekilnojamojo turto ypatumus
#
# import requests
# from bs4 import BeautifulSoup
# import matplotlib.pyplot as plt
# import pandas as pd
#
# url = "https://en.aruodas.lt/gyvenamieji-namai/"
# response = requests.get(url)
# content = response.text
# soup = BeautifulSoup(content, 'html.parser')
#
# skelbimai = soup.find_all('div', class_='list-row-v2 object-row selhouse advert')
#
# duomenys = []
# unikalus = set()     #naudojamas unikaliems
# for skelbimas in skelbimai:
#     kaina = skelbimas.find('span', class_='list-item-price-v2').text.strip()
#     lokacija =skelbimas.select_one('.list_adress-v2 h3').text.strip()   #h3 selektorius-teksto dydis
#     plotas = skelbimas.find('div', class_='list-AreaOverall-v2 list-detail-v2').text.strip()
#     kaina = ''.join(c for c in kaina if c.isdigit())
#
#     unikalus_id = (kaina, lokacija, plotas)
#
#     if unikalus_id not in unikalus:
#         unikalus.add(unikalus_id)
#         duomenys.append({
#             'kaina':kaina,
#             'Lokacija':lokacija,
#             'plotas':plotas
#         })
# df = pd.DataFrame(duomenys)
# print(df)
#
#
