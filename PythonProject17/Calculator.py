# # Import colorama
# # from colorama import Fore, Style
# # colorama.init()


# class Skaiciuotuvas:
#     def __init__(self):
#         self.result = 5
#
#     def sudetis(self, skaicius):
#         self.result += skaicius
#
#     def atimtis(self, skaicius):
#         self.result -= skaicius
#
#     def daugyba(self, skaicius):
#         self.result *= skaicius
#
#     def dalyba(self, skaicius):
#         if skaicius != 0:
#             self.result /= skaicius
#         else:
#             print("Dalyba is nulio negalima")
#
#     def isvalyti(self):
#         self.result = 0
#     def get_result(self):
#         return self.result
#
# Skaiciuoklis = Skaiciuotuvas()
# while True:
#     print("Pasirinkti norima veiksma_>")
#     print("1. Sudetis")
#     print("2. Atimtis")
#     print("3. Daugyba")
#     print("4. Dalyba")
#     print("5. Isvalyti")
#     pasirinkimas = input("Iveskite pasirinkimo numeri_>")
#
#     if pasirinkimas == "1":
#         skaicius = float(input("Iveskite skaiciu_>"))
#         Skaiciuoklis.sudetis(skaicius)
#
#     elif pasirinkimas == "2":
#             skaicius = float(input("Iveskite skaiciu_>"))
#             Skaiciuoklis.atimtis(skaicius)
#
#     elif pasirinkimas == "3":
#             skaicius = float(input("Iveskite skaiciu_>"))
#             Skaiciuoklis.daugyba(skaicius)
#
#     elif pasirinkimas == "4":
#             skaicius = float(input("Iveskite skaiciu_>"))
#             Skaiciuoklis.dalyba(skaicius)
#
#     elif pasirinkimas == "5":
#             Skaiciuoklis.isvalyti()
#     else:
#
#         print("Neteisingas pasirinkimas, bandykite dar karta!")
#     print("result: ", Skaiciuoklis.get_result())
#     print()
#
