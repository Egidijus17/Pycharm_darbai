#
#
# 1.Parašykite programą, kuri atspausdina visus lyginius skaičius nuo 1 iki 10.
#
# sarasas = range(1, 11)
# for skaicius in sarasas:
#     if skaicius %2 == 0:
#         print(skaicius)
#
# Modesto ats.
# for skaicius in range (2, 11, 2) # nuo 2 skaiciaus printina kas antra. (pradinis, galutinis,zingsnis)
#
#
#
# for i in range(1, 11):
#     print(i)
#
#
#
#
#
#
#
#
#
# 2.Sukurkite sąrašą, kuriame yra keletas skaičių. Naudojant for ciklą, apskaičiuokite sąrašo skaičių sumą.
# 1var
# sarasas = [1, 3, 6, 5]
# suma = 0
#
# for skaicius in sarasas:
#     suma = sum(sarasas)
# print(suma)
#
# 2var
# sarasas = [1, 3, 6, 5]
# suma = 0
# for skaicius in sarasas:
#     suma += skaicius
# print("Saraso skaiciu suma:", suma)
#
#
# 3.Parašykite programą, kuri atspausdina visus skaičius nuo 1 iki 20, tačiau jei skaičius yra dalijamas iš 3,
# atspausdinkite "Fizz", jei skaičius yra dalijamas iš 5, atspausdinkite "Buzz", jei skaicius dalinasi is 3 ir is 5
# tada atspausdinti "FizzBuzz"
#
#
# for skaicius in range(1, 21):
#     if skaicius % 3 ==0 and skaicius % 5 ==0:
#         print("Fizz, Buzz")
#     elif skaicius % 3 == 0:
#         print("Fizz")
#     elif skaicius % 5 ==0:
#         print("Buzz")
#     else:
#         print(skaicius)
#
#
#
#
# 4.Sukurkite klasę "KnygosBiblioteka", turinčią atributą
# "knygos" (sąrašą) ir metodus "pridėti_knygą" ir "rodyti_knygas".
# Pridėkite funkcionalumą, kad galėtumėte pridėti knygas į sąrašą ir atspausdinti visas bibliotekoje esančias knygas.
#
#
# class KnygosBiblioteka:
#     def __init__(self):
#         self.knygos = []  #susikuriam tuscia sarasa
#
#     def prideti_knyga(self, knyga):
#             self.knygos.append(knyga)
#     print(f"Knyga sekmingai prideta")
#     def rodyti_knygas(self,):
#         if self.knygos:        #tikrinam ar jau ideta knyga i sarasa
#             print("Knygos: ")
#             for knyga in self.knygos:    #grazina visas knygas esancias sarasa
#                 print(knyga)
#         else:
#             print("Biblioteka tuscia")
#
# knyga = KnygosBiblioteka()             #susikuriam objekta
# knyga.prideti_knyga("Grybu karas")
# knyga.prideti_knyga("Durniu laivas")
# knyga.rodyti_knygas()              #nereikia nieko skliaustuose rasyti, nes def rodyti_knygas prie self nesirasem nieko
#
#
#
#
#
# 5.Sukurkite žodyną su prekių pavadinimais ir jų kainomis. Parašykite programą, kuri suskaičiuoja ir atspausdina
# visų prekių kainų sumą.
#
# prekes = {
#     "obuolys": 1.98,            # obuolys - key, 1.98 - values
#     "persikai": 3.29,
#     "agurkai": 4.50
# }
# suma = 0                   #pradine krepselio suma visada yra lygi 0, todel skaiciuojant suma visada is pradziu suma=0
# for kaina in prekes.values():
#     suma += kaina
# print(f"Visu prekiu kainu suma: {suma}")
# arba
# print("Visu prekiu kainu suma", suma)
#
# 6. naudojant tik FOR nupiesti trikampi
#      *
#     ***
#    *****
#   *******
#  *********
#
#
# eilutes = 6
# for raktas in range(1, eilutes + 1):      #pradeda nuo pirmos eilutes ir eina zemyn + 1
#     print(" " * (eilutes - raktas), end="")  #
#     print("*" * (2 * raktas - 1))
# print(" " * (eilutes - 1), end="")
# print("|")
#
#
# rezultatas:
#
#      *
#     ***
#    *****
#   *******
#  *********
# ***********
#      |
#
