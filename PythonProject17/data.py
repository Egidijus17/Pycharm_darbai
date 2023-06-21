# --------------------------------------------PANDAS(06.21)-----------------------

import pandas as pd
import matplotlib.pyplot as plt

#----vienmate duomenu struktura, kuri saugo vienos eilutes duomenis su indeksais


# data = pd.Series([10, 20, 30, 40, 50])
# print(data)

#----Dvimate duomenu struktura kuri saugo duomenis lenteles pavidalu su stulpeliu ir eiluciu indeksais
#
# data = {'Name': ['Mantas', 'Migle', 'Deividas', 'Ausrine'],
#         'Age': [29, 27, 27, 56],
#         'City': ['Marijampole', 'Vilnius', 'Kaunas', 'Vilkaviskis']
#         }
# df = pd.DataFrame(data)
# print(df)
#----Atvaizduojame pirmas 4 eilutes , renkames buda kaip atvaizduosim, stulpeliu ar pan

# print(df.head())
# print(df.head(2))  #pasirenki skliausteliuose kieki kiek nori atvaizduoti eiluciu is saraso
# print(df['Name'])

# selected_columns = df[['Name', 'City']]  #pasirenkame tik keleta jeigu norime pvz tik name ir tik city
# print(selected_columns)

#prideti nauja stulpeli

# df['Salary'] = [1600, 1400, 1300, 1200]
# print(df)

#grupuokime duomenis pagal miesta ir gaukime vidutini atlyginima

# average_salary_by_city = df.groupby('City')['Salary'].mean()
# print(average_salary_by_city)

#grupavimas pagal amziu

# average_age = df['Age'].mean()
# print(f"Average age: {average_age}")

#filravimas duomenu pagal norima salyga

# filtered_data = df[df['Age']>30][['Name', 'Age']]
# print(filtered_data)
# ----------------------------------darbas su nauja db 'employees.csv'-----------------
df = pd.read_csv('employees.csv')
# print(df.head(5))

#grupuoti pagal 'first_name' stulpeli ir suskaiciuoti jo dydi

group_sizes = df.groupby('FIRST_NAME').size()
# print(group_sizes)

#skaiciuojame salary vidurki  pagal first_name
group_average = df.groupby('FIRST_NAME')['SALARY'].mean()    #vidurkis
# print(group_average)

group_stats = df.groupby('FIRST_NAME')['SALARY'].describe()  #statistika-describe
# print(group_stats)

group_max = df.groupby('FIRST_NAME')['SALARY'].max()     #max
# print(group_max)

group_agg = df.groupby('FIRST_NAME').agg({'SALARY':['sum', 'mean', 'max', 'size']}) #pasirinktas funkcijas,suma,vidurkis,max,kiekis
# print(group_agg)

#atvaizduojam linijine diagrama-------------

# group_agg.plot(kind='line')
#
# plt.title('Suvestines statistika pagal vardus ir ju atlyginima')
# plt.xlabel('Vardas')
# plt.ylabel('Atlyginimas')

# atvaizduojam diagrama
# plt.show()
#atvaizduojam pie diagrama--------------------

# group_agg.plot(kind='pie', sublots=True, figsize=(8, 4))
#
# plt.title('Suvestines statistika pagal vardus ir ju atlyginima')
# plt.xlabel('Vardas')
# plt.ylabel('Atlyginimas')
#
# atvaizduojam diagrama

# plt.show()
#atvaizduojam bar diagrama--------------------
# group_agg.plot(kind='bar', figsize=(8, 4))
#
# plt.title('Suvestines statistika pagal vardus ir ju atlyginima')
# plt.xlabel('Vardas')
# plt.ylabel('Atlyginimas')
#
# # atvaizduojam diagrama
#
# plt.show()

