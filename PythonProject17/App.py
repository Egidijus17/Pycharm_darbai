#------- Objektinis programavimas----------06.13---------

# class Automobilis:
#     def __init__(self, spalva, greitis):
#         self.spalva = spalva
#         self.greitis = greitis
#
#         def didinam_greiti(self, kiekis):
#             self.greitis += kiekis
#
# honda = Automobilis("Juoda", 100)
# print(honda.greitis)

# mazda = Automobilis("Raudona", 200)
# print(mazda.spalva)
#
# honda.didinam_greiti(50)
#
# print("Jusu esamas greitis ", honda.greitis)
#
# class Automobilis:
#     def __init__(self, spalva, greitis):
#         self.spalva = spalva
# #         self.greitis = greitis
# #
# #         def didinam_greiti(self, kiekis):
# #             self.greitis += kiekis
# #
# honda = Automobilis("Juoda", 100)
# print(automobilis.uzvedam_automobili())
# automobilis.didinam_greiti(30)
# print(automobilis.greitis)
# print(automobilis.uzgesom())
# #
# # honda.didinam_greiti(50)
# #
# # print("Jusu esamas greitis ", honda.greitis)
#
# class Automobilis:
#     def __init__(self, spalva, greitis):
#         self.spalva = spalva
#         self.greitis = greitis
#         self.uzvesta = False
#     def uzvedam_automobili(self):
#              if not self.uzvesta:
#             print("Automobilis uzsivede")
#                 self.uzvesta = True
#         else:
#                 print("Masinau jau yra uzvesta")
#
#         def didinam_greiti(self, kiekis):
#             self.greitis += kiekis
#         def uzgesom(self):
#             if self.uzvesta:
#                 print("Automobilis uzgeso")
#                 self.uzvesta = False
#             else:
#                 print("Automobilis jau uzgesintas")


# Funkciju issaukimas

# if __name__ ==

# ------------------------------------------------06.14-19PASKAITA---------------------------------------

# 1.uzduotis sukurti klase "Knyga" su pavadinimu, autoriumi, puslapiais

# class Knyga:
#     def __init__(self, pavadinimas, autorius, puslapiai):
#         self.pavadinimas = pavadinimas
#         self.autorius = autorius
#         self.puslapiai = puslapiai
#          #parasyti metoda kuris patikrintu ar knyga turi daugiau nei 300psl
#     def virs_300_psl(self):
#         if self.puslapiai > 300:
#             return True
#         else:
#             return False
# Knyga1 = Knyga("Haris Poteris", "Rasytoja", 600)
# Knyga2 = Knyga("Karslonas, kuris gyvena ant stogo, "Rasytoja2", 250)
# print(Knyga1.virs_300_psl())
# print(Knyga2.virs_300_psl())

# 2. Sukurti klase kurios vardas darbuotojas, su vardu ,pavarde, atlyginimu.

# class Darbuotojas:
#     def __init__(self, vardas, pavarde, atlyginimas):
#         self.vardas = vardas
#         self.pavarde = pavarde
#         self.atlyginimas = atlyginimas
#         #parasyti metoda, kuris padidins atlyginimas
#
#     def padidinti_atlyginima(self, procentai):
#         padidinimas = self.atlyginimas * procentai / 100
#         self.atlyginimas += padidinimas
#     def pakeisti_pavarde(self, nauja_pavarde):
#         self.pavarde = nauja_pavarde
#         print("Pavarde pakeista sekmingai")
#
#     def visa_informacija(self):
#         print(f" informacija apie darbuotoja: ")
#         print(f"Vardas {self.vardas}")
#         print(f"Pavarde: {self.pavarde}")
#         print(f"Atlyginimas: {self.atlyginimas}")
#
# Darbuotojas1 = Darbuotojas("Jonas", "Jonaitis", 1000)
# Darbuotojas2 = Darbuotojas("Petras", "Petraitis", 1200)
#
# Darbuotojas1.padidinti_atlyginima(10)
# print(f" {Darbuotojas1.vardas}  {Darbuotojas1.pavarde} Naujas atlyginimas: {Darbuotojas1.atlyginimas}")
# Darbuotojas1.pakeisti_pavarde("Kazlauskas")
# print(f" {Darbuotojas1.vardas} {Darbuotojas1.pavarde} pasikeite pavarde!")
#
# print(f"Naujas atlyginimas: {Darbuotojas2.atlyginimas}")
# Darbuotojas1.visa_informacija()

# 3. susiskurti klase preke, turi atributus pavadinimas, kaina, kiekis.
# class Preke:
#     def __init__(self, pavadinimas, kaina, kiekis):
#         self.pavadinimas = pavadinimas
#         self.kaina = kaina
#         self.kiekis = kiekis
#     #atnaujinti kaina(metodas)
#
#     def atnaujinti_kaina(self, nauja_kaina):
#         self.kaina = nauja_kaina
#         print(f" {self.pavadinimas} nauja kaina{nauja_kaina}")
#     def sandelio_likutis(self, pardavimo_kiekis):
#         if pardavimo_kiekis <= self.kiekis:
#             self.kiekis -= pardavimo_kiekis
#             print(f"parduota {self.pavadinimas} {pardavimo_kiekis}")
#         else:
#             print(f"Nepakanka prekiu: {self.pavadinimas}")
#
#     def sandelio_papildymas(self, padidintas_likutis):
#         self.kiekis += padidintas_likutis
#         print(f"Padidinta{self.pavadinimas} {padidintas_likutis}")
#         #sukuriamas objektas
# Preke1 = Preke("Pienas", 5, 50)
# Preke2 = Preke("Kiausiniai", 3, 10)
#
# Preke1.atnaujinti_kaina(2.20)
#
# # 4. pranesti pirkejui, kad mes neturim tiek prekiu
#
# Preke1.sandelio_likutis(8)
# Preke1.sandelio_papildymas(15)
# print(Preke1.kiekis)
# print("Sandelio likutis", Preke1.kiekis)

#------------------------- 5. Blogo kurimas------------------------------
#
# class Blog:
#     def __init__(self):
#         self.posts = []
#     def create_post(self, pavadinimas, aprasymas):
#         post = {
#             "pavadinimas": pavadinimas,
#             "aprasymas": aprasymas
#         }
#
#         self.posts.append(post)
#         print("Irasas sekmingai sukurtas")
#
#
#     def display_all_posts(self):
#         if not self.posts:
#             print("No blog post found")
#         else:
#             print("Blog posts: ")
#             for post in self.posts:
#                 print(f" pavadinimas: {post['pavadinimas']}")
#                 print(f" aprasymas: {post['aprasymas']}")
#                 print("-------")
#     def update_post(self, pavadinimas, atnaujinimas):
#         for post in self.posts:
#             if post["pavadinimas"] == pavadinimas: #cia yra salyga, todel turi buti tas pats title
#                post["aprasymas"] = atnaujinimas #updateinama vieta rasosis us viena lygybe =
#                print("Blog post updated")
#                break
#         else:
#             print("Blog post not found")
#     def delete_post(self, pavadinimas):
#         for post in self.posts:
#             if post ["pavadinimas"] == pavadinimas:
#                 self.posts.remove(post)
#                 print("Postas buvo pilnai pasalintas")
#                 break
#         else:
#             print("Postas nebuvo pasalintas")
#
#
# post1 = Blog()
# # naudojame ta pati objekta nes jis neturi atributu
#
# post1.create_post("duomenu analitikos studentai uzkariavo pasauli", "Karta gyveno analitikai, kurie ismoks programuoti")
# post1.create_post("Mokslininkai isrado nauja metoda", "Kaip greiciau simokti duomenu analize")
# post1.create_post("Kulinarijos sedevrai", "Tukstantis receptu")
#
# post1.display_all_posts()
# post1.update_post("duomenu analitikos studentai uzkariavo pasauli", "trampampamtralialia" )
# post1.display_all_posts()
# post1.delete_post("duomenu analitikos studentai uzkariavo pasauli")
# post1.display_all_posts()
# #CRUD create, read, update, delete
#
#






