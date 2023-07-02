# ---------------------NUMPY biblioteka-skaiciavimui-----------------------------------------------
# #
# import numpy as np
# import matplotlib.pyplot as plt
# import pandas as pd

#sukuriame masyva( np array)

# arr = np.array([1, 2, 3, 4, 5])
# print(arr)

# arr = np.array([1, 2, 3])
# arr2 = np.array([4, 5, 6])
# result = arr + arr2
# print(result)

# arr = np.array([1, 2, 3])   #kelimas kvadratu
# result = np.square(arr)

# arr = np.array([1, 2, 3])   #kelimas kvadratu
# result = np.square[arr]


#indeksavimas
#
# arr = np.array([1, 2, 3])
# result = np.square[arr]
# value = arr[1]
# print(value)

# array slicing   - isskiriam kelias reiksmes
# arr = np.array([1, 2, 3, 4, 5])
# value = arr[1]
# sliced_arr = arr[1:4]
# print((sliced_arr))

# array slicing   - isskiriam kelias reiksmes
# arr = np.array([1, 2, 3, 4, 5])
# value = arr[1]
# sliced_arr = arr[3:]
# print((sliced_arr))

# array slicing   - isskiriam kelias reiksmes
# arr = np.array([1, 2, 3, 4, 5])
# value = arr[1]
# sliced_arr = arr[-3:]
# print((sliced_arr))

# suma,max,min,mean

# matrica = np.array(([1, 2, 3], [4, 5, 6], [7, 8, 9]))
# print(matrica)

#daugyba
# matrica = np.array(([1, 2, 3], [4, 5, 6], [7, 8, 9]))
# matrica2 = np.array([[10, 11, 12], [13, 14, 15], [16, 17, 18]])
# daugyba = np.dot(matrica, matrica2)
# print(daugyba)
# daugyba = [0,0] = (1*10) + (2*13) + (3*16) = 84  -----------------paaiskinimas

# random_numbers = np.random.randint(0,10, size=5)  meta 5 skaicius random nuo 0 iki 10
# print(random_numbers)

# numbers = np.linspace(0, 1, 5)   #sugeneruoja 5 skaicius nuo 0 iki 1
# print(numbers)
#
# sequence = np.arange(10)   # sugeneruoja skaiciu seka iki 10 siuo atveju
# print(sequence)

# x = np.linspace(0, 10, 100)            #linijine sinusoide
# y = np.sin(x)#
# plt.plot(x, y)
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('Sinusine funkcija')
# plt.show()

# x = np.random.rand(100)                  #taskine
# y = np.random.rand(100)
# plt.scatter(x,y)
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('Random points')
# plt.show()

# data = np.random.randn(1000)    #randn atsitiktiniai skaiciai ir rodo kieki toje dimensijoje
# plt.hist(data, bin=20)
# plt.xlabel('Values')
# plt.ylabel('Frequency')
# plt.title('Histogram')
# plt.show()

#salygu taikymas

# masyvas = np.array(1, 2, 3, 4, 5)
# daugiau_uz_du = masyvas[masyvas > 2]
# print(daugiau_uz_du)


# masyvas = np.array([1, 2, 3, 4, 5])

# daugiau_uz_du = masyvas[masyvas > 2]
# print(daugiau_uz_du)

# daugiau_uz_du = np.where[masyvas > 2]
# print(daugiau_uz_du)

# arr1 = np.array([True, False, True])
# arr2 = np.array([False, True, True])
# result = np.logical_and(arr1, arr2)
# print(result)

# arr = np.array([1, 2, 3, 4, 5, 6])
# change_arr = np.reshape(arr, (2,3))
# print(change_arr)

# arr = np.array([1, 2, 3, 4, 5, 6])
# splitting = np.split(arr, 3)
# print(splitting)

# arr = np.array([4, 3, 2, 1, 5, 6])
# sorting = np.sort(arr)


# arr = np.array([4, 4, 3, 2, 1, 10, 1, 5, 6, 6, 6])
# unique = np.unique(arr)
# print((unique))
# --------------------------------------------------------------------------------------
# uzduotis
#duomenu sarasas su akciju kainu reiksmemis
# akcijos = np.array([100, 110, 120, 115, 120, 105, 95, 100])
# # apskaiciuojame dienos pelna ir nuostoli
# dienos_pelnas = akcijos[1:] - akcijos[:-1]
# dienos_nuostolis = akcijos[:-1] - akcijos[1:]
# # randame diena su didziausia ir maziausia akciju kaina
# didziausia_reiksme = np.max(akcijos)
# didziausios_reiksme_indeksas = np.argmax(akcijos)
# maziausia_reiksme = np.min(akcijos)
# maziausios_reiksmes_indeksas = np.argmin(akcijos)
# # apskaiciuojame akciju kainos svyravimas
# kainos_svyravimas = np.ptp(akcijos)
#
# print(f'Dienos pelnas: {dienos_pelnas}')
# print(f'Dienos nuostolis: {dienos_nuostolis}')
# print(f'Didziausia akciju kaina: {didziausia_reiksme}, diena: {didziausios_reiksme_indeksas +1}')
# print(f'maziausia akciju kaina: {maziausia_reiksme}, diena: {maziausios_reiksmes_indeksas +1}')
#
# print(f'Akciju kainos svyravimas: {kainos_svyravimas}')

# nupiesti linijine diagrama--------------------
# plt.plot(range(1, len(akcijos) + 1), akcijos, marker='o')
# plt.title('Akciju kainos')
# plt.xlabel('Diena')
# plt.ylabel('Kaina')
# #zymime didziausia ir maziausia reiksmes
# plt.plot(didziausios_reiksme_indeksas + 1, didziausia_reiksme, marker='o', color='red', label='didziausia')
# plt.plot(maziausios_reiksmes_indeksas + 1, maziausia_reiksme, marker='o', color='green', label='maziausia')
# #rodyti legenda
# plt.legend()
# #rodyti diagrama
# plt.show()

# ---------------------------------06.30---------------------------------------------------


# temperaturos

# temperaturos = np.array([20, 22, 23, 19, 25, 21, 20, 18, 24, 26, 22, 21, 20, 25, 23, 21, 19, 20, 22, 24, 26, 21, 23, 25,
#                          26, 22, 20, 21])

# #apskaiciuojame vidutine temparatura
#
# vidutine_temperatura = np.mean(temperaturos)
# # print((vidutine_temperatura))
#
# #apskaiciuoajame didziausia temparatura
#
# didziausia_temperatura = np.max(temperaturos)
# # print(didziausia_temperatura)
#
# maziausia_temperatura = np.min(temperaturos)
# # print(maziausia_temperatura)
#
# slenkscio_verte = 23
#
# #randame dienas kai temperatura virsija slenkscio verte
#
# virsijo_slenkstine_temp = temperaturos[temperaturos > slenkscio_verte]
# # print(f'Dienos, kai temperatura virsijo slenkstine verte: {virsijo_slenkstine_temp}')

#nubereziame grafika naudojant matplotlib ir pandas
# df = pd.DataFrame({'Temperatura': temperaturos})
#
# slekstis = 23
#
# filtruojame_df = df[df['Temperatura'] > slekstis]
#
# plt.plot(df.index. df['Tempertaura'], label='Temperatura')
# plt.scatter(filtruojame_df.index, filtruojame_df['Temperatura'], color='red', label='Virsijo slenksti')
# plt.axhline(y=slenkstis, color='gray', linestyle='--', label='Slenkscio verte')
# plt.xlabel('Dienos')
# plt.ylabel('Temperaturos')
# plt.title('Kasdienine temperatura')
# plt.legend()
# plt.show()

# -------------------------------------------Uzduotis--------------------------------------------
#
# 1. Apsirašykite duomenų rinkinį su pirkinių krepšelio prekių ir jų kainų informacija.
# Naudodami NumPy ir Matplotlib:
# Apskaičiuokite bendrą pirkinių krepšelio sumą. Raskite brangiausią ir pigiausią prekę.
# Sudarykite pie diagramą, kurioje rodomi skirtingų prekių dalis bendroje sumoje.

# prekes = np.array(['Pienas', 'Duona', 'Svietas', 'Agurkas'])
# kaina = np.array([1.5, 1.8, 1.9, 2.2])
# kiekis = np.array([1, 2, 4, 5])
# krepselio_suma = np.dot(kaina, kiekis)
# print(f'Pirkiniu krepselio suma: {krepselio_suma}')
# brangiausia_preke = prekes[np.argmax(kaina)]
# print(f'Brangiausia preke: {brangiausia_preke}')
# pigiausia_preke = prekes[np.argmin(kaina)]
# print(f'Pigiausia preke: {pigiausia_preke}')

# fig, ax = plt.subplots()
# ax.pie(kiekis * kaina, labels=prekes, autopct='%1.1f%', startangle=90) #nurodo kad bus 1 skaicius po kablelio ir su procento zenklu
# ax.axis('equal')
#
# plt.tile('Prekiu krepselis')
# plt.show()

# ------------------------------------------------------------------------------------------------------------
# 2. Aprašykite duomenų rinkinį, kuriame yra metiniai pardavimų duomenys.
#
# Naudodami NumPy ir Matplotlib:
#     1.Apskaičiuokite metinį pardavimų sumažėjimą procentais kiekvieniems metams.
#     2.Sukurkite linijinę diagramą, kurioje rodomi metiniai pardavimų pokyčiai.
#     3.Naudojant NumPy funkcijas, apskaičiuokite tendencijos liniją, kuri prognozuotų ateities pardavimų pokyčius.
#     4.Atvaizduokite tendencijos liniją kartu su esamais duomenimis.

# #
# pardavimai = np.array([100, 200, 150, 300, 250])
# metai = np.array([2018, 2019, 2020, 2021, 2022])
# #1
# pardavimu_pokytis = (pardavimai[1:] - pardavimai[:-1]) / pardavimai[:-1] * 100
# print(pardavimu_pokytis)
#  #2
# plt.plot(metai[1:], pardavimu_pokytis, marker='o', color='pink')
# plt.xlabel('Metai')
# plt.ylabel('Pardavimu pokytis', '%')
# plt.title('Metiniai pardavimu pokyciai')
#  #3
# tendencija = np.polyfit(metai[1:], pardavimu_pokytis, 1)
# prognoze = np.polyval(tendencija, metai[1:])
#
# plt.plot(metai[1:], prognoze, color='red', label='prognoze')
# plt.legend()
# plt.show()
#
# #4