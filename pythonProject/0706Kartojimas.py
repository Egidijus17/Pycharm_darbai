#-----------------KARTOJIMAS(07.06)------------------------------------------------------------
# -----------------Automatinis duomenu analizes ir vizualizavimo irankis-------------------------
#
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
#
# def load_data(file):
#     data = pd.read_csv(file, encoding='utf-8')
#     return data
# def clean_data(data):
#     cleaned_data = data.drop_dublicates()
#     cleaned_data['amzius'] = cleaned_data['amzius'].astype(int)
#     cleaned_data['vardas'] = cleaned_data['vardas'].str.strip()
#     cleaned_data['pavarde'] = cleaned_data['pavarde'].str.replace(' ', '')
#     cleaned_data = data.dropna()
#     return cleaned_data
#
# def perform_calculation(data):
#     calculatios = {}
#     calculatios['average age'] = data['amzius'].mean
#     calculatios['age range'] = np.ptp(data['amzius'])   #ptp. iesko range, bet grazina skirtuma
#     return calculatios
# def visualize_data(data):
#     age_counts = data['amzius'].value_counts().sort_index()
#
#     plt.figure(figsize=(10, 6))
#     plt.bar(age_counts.index, age_counts.values)
#     plt.xlabel('amzius')
#     plt.ylabel('pasikartojimai')
#     plt.title('amziaus pasiskirstymas')
#     plt.show()
#
# def main():
#     file_path = 'duomenys.csv'
#     data = load_data(file_path)
#     # cleaned_data = clean_data(data)
#     calculations = perform_calculation(cleaned_data)
#     print('skaiciavimai: ')
#     for key, value in calculations.items():
#         print(f'{key}: {value}')
#
#     visualize_data(cleaned_data)
#     if __name__ == '__main__':
#         main()


# 2. Užduotis is testo(06.29):
#      [+] Naudodami pandas, nuskaitykite CSV failą "duomenys.csv" ir
# įrašykite duomenis į PostgreSQL duomenų bazės "students" lentelę.
#      [+] Papildoma sąlyga: Įrašykite duomenis į "students" lentelę tik tuomet, jei amžius yra didesnis nei 20.

# import pandas as pd
# import matplotlib.pyplot as plt
#
# data = pd.read_csv('duomenys.csv', encoding="utf8")
# filtered_data = data[data['amzius'] > 20]
# print(filtered_data)




# 3. Užduotis is testo(06.29):
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

