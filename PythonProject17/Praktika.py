
# -------------------ZODYNA(dictionaries)----------------------------------
#
# zmogus = {
#     "vardas": "Jonas",
#     "amzius": 27,
#     "miestas": "Vilnius"
# }
# print("Mano vardas: ", zmogus['vardas'])
#
# zmogus["Lytis"] = "Vyras"
# #pridedame nauja elementa i savo zodyna
# print("As esu ", zmogus["Lytis"])
# #keiciame reiksmes
# zmogus["amzius"] = 20
# print("Atsiprasau man yra: ", zmogus["amzius"], "metu")
#
# #triname reiksmes
#
# del zmogus["miestas"]
# print(zmogus['miestas'])
#
# #iteruojame per visus zodyno elementus
#
# for key, value in zmogus.items():
#     print(key, ":", value)

# ---------------------------Tuple(kortele)--------------------------------

# kordinates = (10, 50)
# print(kordinates[1])
#
# kordinates1 = (54, 42, 12)
#
# sujungtos_kordinates = kordinates + kordinates1
# print(sujungtos_kordinates)

# ------------------------------------06.16---------------------------------------------------------

#---------------------------------- PAVELDEJIMAS------------------------------------------
#metodo perrasymas!!!!!!!!!!!!!!!!!!!


# class Animal:
#     def __init__(self, name):
#         self.name = name
#     def make_sound(self):
#         print("The animal make a sound")
#
# class Dog(Animal):
#     def __init__(self, name, age):
#         super().__init__(name)   # super - pasiima savybes is ir vaikine klase Dog pasiekia tevines klases metodus ir iskviesti juos
#         self.age = age
#     def make_sound(self):
#         print("The dog barks")
#
# dog = Dog("Bob", 5)
# dog.make_sound()
# # print(dog.name, dog.age)
# print(f"My dog name is {dog.name}" + " and age is " + str(dog.age))



# class Vehicle:
#     def __init__(self, brand):
#         self.brand = brand
#
#     def start_engine(self):
#         print("Engine started")
#
#     def stop_engine(self):
#         print("Engine stopped!")
#
# class Car(Vehicle):
#
#     def drive(self):
#         print("Car is driving!")
#
# car = Car("Toyota")
# print(car.brand)
# car.start_engine()
# car.drive()
# car.stop_engine()
# ----------------------------------------------------------------------------

#sukurti klase zmogus, tures varda ir metus. sukurti metoda kuris atvaizduos jo visa info, varda ir amziu

# class Zmogus:                                #sukuriam tevine klase Zmogus
#     def __init__(self, name, age):           #Isvardinam savybes
#         self.name = name                     #Aprasome savybes
#         self.age = age                       #Aprasom savybes
#     def display_info(self):                        #metodas rodyti info apie zmogu
#         print(f"Zmogaus vardas yra {self.name}")
#         print(f"Zmogaus amzius yra {self.age}")
#         #sukurti
#
# class Darbuotojas(Zmogus):               #sukuriame vaikine klase(INHERITANCE) Darbuotojas
#     def __init__(self, name, age, salary):  #isvardiname kokiu savybiu tures darbuotojas
#         super().__init__(name, age)        #nurodome kokia savybes paveldetas is zmogaus klases
#         self.salary = salary               #aprasome papildoma darbuotojo savybe
#
#     def display_info(self):
#         super().display_info()                  #panaudosim tevines klases metoda
#         print(f"Darduotojo atlyginimas yra {self.salary}")
#
# zmogus = Zmogus(" Antanukas", 12)                 #sukuriame tevines klases objekta
# darbuotojas = Darbuotojas(" Jonukas", 25, 2000)   #sukuriame vaikines klases objekta
#
# zmogus.display_info()
# print()
# darbuotojas.display_info()

# ---------------------------------------------------------------------------------------------------

# sukurti pirkiniu krepselio funkcionaluma. Turim produkta ir turim krepseli

# class Product:
#     def __init__(self, title, price):
#         self.title = title
#         self.price = price
#
#
#     def display_info(self):
#         print(f" Produkto pavadinimas yra {self.title}")
#         print(f" Produkto kaina {self.price} $")
#
# class DiscountedProduct(Product):
#
#
#     def __init__(self, title, price, discount_percentage):
#         super().__init__(title, price)
#         self.discount_percentage = discount_percentage
#
#
#     def calculate_discounted_price(self):
#         discount_amount = self.price * (self.discount_percentage / 100)
#         discounted_price = self.price - discount_amount
#         return discounted_price
#
#     def display_info(self):
#         super().display_info()
#         print(f" Nuolaida {self.discount_percentage} %")
#         print(f" Galutine kaina {self.calculate_discounted_price()} $")

# class ShoppingCart(Product):
#     def __init__(self):
#         super().__init__(title=None, price=None)
#         self.products = []
#
#     def add_product(self, product):
#         self.products.append(product)
#         print(f" Produktas {product.title} pridetas i krepseli ")
#
#
#     def remove_product(self, product):
#         if product in self.products:
#             self.products.remove(product)
#             print(f" Produktas {product.title} pasalintas is krepselio ")
#         else:
#             print(f" Produktas {product.title} nerastas krepselyje")
#
# #suskaiciuoti bendra suma(calculate total price)
#
#     def calculate_total_price(self):
#         total_price = 0
#         for product in self.products:
#             total_price += product.price
#         return total_price
#
#
#
# prod = Product("Pienas", 2.99)
# prod1 = DiscountedProduct ("Obuolys", 1.99, 15)
# prod2 = Product("Sviestas", 4.99)
#
# shoppingcart = ShoppingCart()
# shoppingcart.add_product(prod)
# shoppingcart.add_product(prod1)
# shoppingcart.add_product(prod2)
# print()
# for product in shoppingcart.products:
#     product.display_info()
#     print()
#
# total_price = shoppingcart.calculate_total_price()
# print(f" Bendra krepselio kaina {total_price} $ ")
# print()
#
# shoppingcart.remove_product(prod)
# total_price = shoppingcart.calculate_total_price()
# print((f" Nauja bendra kaina {total_price} $ "))
# ----------------------------------------------------------------------------------------------------------------------
# print("Egidijus", "Vilkas", "1983 07 14")
# print("Egidijus\nVilkas\n1983 07 14")
# print("2+5 yra", 2+5)
# print("5**5 = ",5**5)

# print("STOP!")
# Egidijus = input("Kas cia eina?")
# print("Gali praeiti", Egidijus)

skaicius = float(input("Ivesk skaiciu: "))
# sveikasSkaicius = int(input("Ivesk sveika skaiciu: "))
# tekstas = input("Ivesk teksta: ")
# print("skaičius =", skaicius)
# print("skaičius yra", type(skaicius))
# print("skaičius * 2 =", skaicius * 2)
# print("sveikas skaičius =", sveikasSkaicius)
# print("sveikas skaičius yra", type(sveikasSkaicius))
# print("sveikasSkaičius * 2 =", sveikasSkaicius * 2)
# print("tekstas =", tekstas)
# print("tekstas yra", type(tekstas))
# print("tekstas * 2 =", tekstas * 2)