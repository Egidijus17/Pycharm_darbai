
# # ---------------------------------------------06.27(26pamoka)----------------------------------------------------
# import pandas as pd
# import matplotlib.pyplot as plt
# from pathlib import Path
# filename = Path("C:/Users/Patricija/OneDrive/Desktop/PYTHON/sales_data_sample.csv")
# df = pd.read_csv(filename, encoding="ISO-8859-1")
# print(df.head(5))


# 1.Suskirstykite klientus pagal šalį.

# group_by_country = df.groupby('Country')
# print(group_by_country)
#
# plt.figure(figsize=(12, 6))
# group_by_country.size().plot(kind='bar')
#
# plt.title('Salys pagal uzsakyma')
# plt.xlabel('Salis')
# plt.ylabel('klientai')
# plt.show()


# 2.Atrinkite užsakymus, kurių suma viršija 1000 eurų

# group_by_order = df[df['Sales']>1000]
# print(group_by_order)

# df['Total'] = df['QUANTITYORDERED'] * df['PRICEEACH']
# group_by_order = df[df['Total'] > 5000][['CUSTOMERNAME', 'Total']]
# df.to_csv('sales_data_sample.csv', index=False)            --------#nebutinas#ikeliam nauja stulpeli i lentele
# print(group_by_order)

# 3.Išfiltruokite užsakymus, kurie buvo pristatyti nuo 2003/9/30 iki 2005/3/15 .

# df['ORDERDATE']=pd.to_datetime(df['ORDERDATE'], format='%d/%m%Y %H:%M', errors='coerce')
# filtered_data = df[(df['ORDERDATE'] >='9/9/2003') & (df['ORDERDATE']<='3/3/2005')]
# print(filtered_data)

# 4.Išfiltruokite užsakymus, kurių statusas 'Disputed';

# disputed = df[df['STATUS']=='Disputed']
# print(disputed)


# 5.Sukurkite skritulinę diagramą, kurioje būtų pavaizduota klientų skaičiaus pasiskirstymas pagal šalis

# group_by_country = df.groupby('Country')
# print(group_by_country)
#
# plt.figure(figsize=(12, 6))
# group_by_country.size().plot(kind='pie')
#
# plt.title('Salys pagal uzsakyma')  #taisyti pagal uzduoty
# plt.xlabel('Salis')         #taisyti
# plt.ylabel('klientai')      #taisyti
# plt.show()

# group_by_country = df['COUNTRY'].value_counts()           #diagramu tvarkymas
# plt.bar(group_by_country.index, group_by_country.values)
# plt.xlabel('Country')
# plt.ylabel('Customername')
# plt.xticks(rotation=90)
# plt.show()

# group_by_country = df['COUNTRY'].value_counts().nlargest(10)    #parodo 10 didziausiu saliu
# plt.bar(group_by_country.index, group_by_country.values)
# plt.xlabel('Country')
# plt.ylabel('Customername')
# plt.xticks(rotation=90)   #diagramu tvarkymas
# plt.show()


