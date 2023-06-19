
#
# Parašykite programą, studentų valdymo sistemą ir leistų vartotojui įvesti komandas, kad galėtų manipuliuoti studentų duomenimis.
#
#     1.Pridėti naują studentą
#     2.Pašalinti studentą
#     3.Gauti informaciją apie studentą pagal studento ID
#     4.Rodyti visus studentus
#     5.Baigti programą



# studentu_sarasas = ["Jonas Jonaitis", "Petras Petraitis", "Ona Onaite"]
# studentu_sarasas.append("Maryte Maraityte")
# print(studentu_sarasas)
#     def prideti_nauja_studenta(self):
#         print(prideti_nauja_studenta())






















#Mindaugo sprendimas:
# class Student:
#     def __init__(self, name, id):
#         self.name = name
#         self.id = id
#
#     def __str__(self):
#         return self.name + " " + str(self.id)
#
#
# def choose_action():
#     return int(input(
#         'choose action: 1: add student, 2: remove student, 3. get student info by id 4. get all students 5: exit: '))
#
#
# students = []
# action = None
#
# while action != 5:
#     action = choose_action()
#
#     if action == 1:
#         name = input('enter name: ')
#         id = int(input('enter id: '))
#         students.append(Student(name, id))
#
#     elif action == 2:
#         id = int(input('enter id: '))
#         for student in students:
#             if student.id == id:
#                 students.remove(student)
#
#     elif action == 3:
#         id = int(input('enter id: '))
#         for student in students:
#             if student.id == id:
#                 print(student)
#
#     elif action == 4:
#         for student in students:
#             print(student)
#
#     elif action == 5:
#         print('bye')
#
#     else:
#         print('wrong action')
#         action = choose_action()