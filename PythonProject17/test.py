# 1. Užduotis:
#      [+] Sukurkite klasę "Automobilis" su savybėmis "marke" ir "metai".
#      [+] Sukurkite metodą "informacija", kuris išveda automobilio informaciją.
#      [+] Sukurkite vaikinę klasę "ElektrinisAutomobilis", kuri paveldi klasę "Automobilis" ir
# papildomai turi savybę "baterijos_talpa" ir metodą "baterijos talpa informacija",
# kuris išveda informaciją apie automobilio baterijos talpą.

# class Automobilis:
#     def __init__(self, marke, metai):
#         self.marke = marke
#         self.metai = metai
#     def display_info(self):
#         print(f"Automobilio marke yra {self.marke}")
#         print((f"Automobilio metai yra {self.metai}"))
#
# class ElektrinisAutomobilis(Automobilis):
#
#     def __init__(self, marke, metai, baterijos_talpa):
#         super().__init__(marke, metai)
#         self.baterijos_talpa = baterijos_talpa
#     def display_info(self):
#         super().display_info()
#         print(f"Baterijos talpa yra {self.baterijos_talpa}")
#
# automobilis = Automobilis("Audi", 2020)
# Elektromobilis = ElektrinisAutomobilis("Tesla", 2022, 88)
#
# automobilis.display_info()
# print()
# Elektromobilis.display_info()

# 2. Užduotis:
#      [+] Naudodami pandas, nuskaitykite CSV failą "duomenys.csv" ir
# įrašykite duomenis į PostgreSQL duomenų bazės "students" lentelę.
#      [+] Papildoma sąlyga: Įrašykite duomenis į "students" lentelę tik tuomet, jei amžius yra didesnis nei 20.

# import pandas as pd
# from pathlib import Path
# import matplotlib.pyplot as plt
# file_path = Path('duomenys.csv')
# df = pd.read_csv(file_path)
# df = pd.DataFrame(data)
# import psycopg2
# db_params = {
#     'host': 'localhost',
#     'port': 5432,
#     'database': 'students',
#     'user': 'postgres',
#     'password': 'pswd'
#   }
# def create_table():
#     connection = psycopg2.connect(**db_params)
#     cursor = connection.cursor()
#     create_table_query="""
#
#     """





# 3. Užduotis:
#      [+] Išskirkite produktų pavadinimus iš
# {https://www.rde.lt/categories/lt/1599/sort/5/filter/0_0_0_0/page/1/Dvira%C4%8Diai.html}
# puslapio naudodami Beautiful Soup ir išsaugokite juos į Pandas DataFrame stulpelį.

# import requests
# from bs4 import BeautifulSoup
# import pandas as pd
# import matplotlib.pyplot as plt
#
# url = "https://www.rde.lt/categories/lt/1599/sort/5/filter/0_0_0_0/page/1/Dvira%C4%8Diai.html"
#
# response = requests.get(url)
# soup = BeautifulSoup(response.content, 'html.parser')
# product_names = soup.find_all('span', class_= )

# 4. Užduotis:
#     [+] Išskirkite informaciją apie produktų kainas ir jų kategorijas iš pigu.lt puslapio naudodami Beautiful Soup
# ir išsaugokite juos į Pandas DataFrame.
#     [+]  Remdamiesi gautais duomenimis sukurkite stulpelinę diagramą,
# kurioje bus pavaizduotos produktų kainos pagal kategorijas mažėjančia tvarka.

