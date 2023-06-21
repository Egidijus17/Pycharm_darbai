#
# ----------------------Random------------------------------------------
#
# import random
# import time
# studentai = ["Rugile", "Egidijus", "Deividas", "Tomas", "Migle", "SausliusS", "SauliusA", "Ausrine", "Jurate",
#              "Vaidas", "Mantas", "Modestas"]
# random_student = random.choice(studentai)
# time.sleep(3)
# print("Atsitiktinai pasirinktas studentas: ", random_student)
#
# -------------------------------------SETTER,GETTER-06.16----------------------------------------
#
# class Person:
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def get_name(self):   #gaunam reiksmes
#         return self.name
#     def set_name(self, name):  #nustatom reiksmes
#         self.name = name
#
#     def get_age(self):
#         return  self.age
#     def set_age(self, age):
#         if age >= 0:
#             self.age = age
#         else:
#             print("Amzius negali buti neigiamas")
#
# person = Person("Jonas", 15)
#
# print("name", person.get_name())
# print("age", person.get_age())
#
# person.set_name("Petras")
# person.set_age(22)
#
# print("new_name", person.get_name())
# print("new_age", person.get_age())