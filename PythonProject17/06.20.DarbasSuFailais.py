#
# # ---------------------------------- DARBAS SU FAILAIS-----------------------------------
# #
# # Darbas su failais naudijant open funkcija:
# #
#                                                                    #"a" - append
# file = open("failopavadinimas.txt", "a", encoding="utf8")                          #"r" - read - nuskaito, "w" - write - paraso
# content = file.write("Tekstas naujame faile, kuriame išbandome open funkcija")
# print(content)
#
# file = open("failopavadinimas.txt", "a", encoding="utf8")                          #"r" - read - nuskaito, "w" - write - paraso
# file.write("Tekstas naujame faile, kuriame išbandome open funkcija")      #encoding - supranta ltu raides
# file.close()                                                             #uzdaro faila, ty baigia veiksma
#
#
# with open("failopavadinimas.txt", "w", encoding="utf8") as file:     #tinkamai atidaro ir uzdaro failus, nedubliuoja teksto
#     file.write("Tekstas antrajame faile\n")
#     file.write("Antra eilute\n")
#     file.write("Trecia eilute\n")
#
# filename = input("Iveskite failo pavadinima-> ")
#
# try:
#     with open(filename, "r", encoding="utf8") as file:
#         content = file.read()
#         print("File content: ")
#         print(content)
# except FileNotFoundError:
#     print("File not found!")
# except:
#     print("Something went wrong!")
#
# file = open("Naujasfailas.txt", "w", encoding="utf8")
# content = file.write("Naujo failo naujas tekstas")
# print(content)
# file = ("Iveskite naujo failo pavadinima-> ")
# try:
#     with open("Naujasfailas.txt", "w", encoding="utf8") as file:
#         file.write("Bandymas kurti faila\n")
#         file.write("Manau pavyko\n")
#         file.write("Puiku, Egidijau!")
#         print("Duomenys irasyti")
# except:
#     print("Tu dar nesimokai!")
#
