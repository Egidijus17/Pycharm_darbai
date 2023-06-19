------------------------------------- 17 PASKAITA---------------------------------------------------------------------
# komentuoja viena eilute

"""
Multi uzkomentavimas
"""

vardas = "Egidijus"
amzius = 24
amzius = "24"
print(vardas)
print(amzius)
print(type(vardas))

arVartotojasAktyvus = False

print(type(arVartotojasAktyvus))

produktoKaina = 3.99

print(type(produktoKaina))

sarasas = [rasomos reiksmes]

miestai = ["Vilniuje", "Kaunas", "Klaipeda"]
print(len(miestai))


print(miestai)
print("As gyvenu " + miestai[0])
print("Mano vardas " + vardas + " As gyvenu " + miestai[0] +  "mano amzius" +  str(amzius))
miestai[1] = "Siauliai"


miestai.append("Panevezys")
print(miestai)

miestai.insert(1, "Anyksciai")

miestai.pop() issitrina paskutinis kintamasis

del miestai[2] istrina pagal nurodyta vieta

-------------------------IF-----------------------------------------

if salyga == amzius:--------

if amzius >= 18:
    print("Pilnametis")
else:
    print("Nepinamtis")

elif - keleta salygu

if amzius >= 18:
    print("Pilnametis")

elif amzius>= 24:
    print("Daugiau nei 18")
elif amzius>25:
    print("Daugiau nei 25")
else:
    print("Nepilnametis")

skaiciuSarasas = [1, 3, 123, 1245, 12312]
print(len(miestai))
if len(skaiciuSarasas) > 0:
    print("Skaiciu sarasas pilnas")
else:
    print("Skaiciu sarasas tuscias")

zodis = "Kaunas"
miestai = ["Vilniuje", "Kaunas", "Klaipeda"]

if zodis in miestai:
    print("Zodis " + zodis + " egzistuoja sarase")

else:
    print("Zodis nerastas")

skaiciuSarasas = [1, 3, 123, 1245, 12312]

skaicius = int(input("Iveskite skaiciu: "))

if skaicius > 0:
    print("Skaicius yra teigiamas")
elif skaicius <0:
    print("Skaicius yra neigiamas")
else:
    print("Skaicius yra nulis")

# -------------------OPERATORIAI---------------------
"""
-------------------PRISKIRIMO OPERATORIAI------------------
= PRISKIRIMAS
+= PRIDEDA IR PRISKIRIA
-= ATIMA IR PRISKIRIA
*=
/=
%=
------------------------MATEMATINIAI OPERATORIAI----------------------
+
-
*
/
%
** KELIMAS LAISPNIU
// SVEIKOJI DALYBA

---------------------------PALYGINIMO OPERATORIAI---------------------
== LYGU
!= NELYGU
<
>
<= MAZIAU LYGU
>= DAUGIAU LYGU

------------------------------LOGINIAI OPERATORIAI--------------
and
or
not
-----------------NARYSTES OPERATORIAI------------------
in -PRIKLAUSO
not in -NEPRIKLAUSO

-------------------TAPATUMO OPERATORIAI(IDENTITY OPERATORS)---------------
is  YRA
is not NERA

"""
------------------UZDUOTYS-----------------------------------------------
# 1. Patikrinkite, ar studentas išlaikė egzaminą;

ivertinimas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
islaikymoRiba = 5
ivertinimas = int(input("Iveskite ivertinima"))
if ivertinimas >= islaikymoRiba:
    print("Egzaminas islaikytas")
else:
    print("Egzaminas neislaikytas")



# 2. Patikrinkite, ar skaičius yra lyginis;

Skaiciai = 4

if Skaiciai % 2 == 0:
    print("Lyginis skaicius")
else:
    print("Nelyginis skaicius")


# 3. Patikrinkite, ar sąraše yra bent du skaičiai

sarasas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

if len(sarasas) >= 2:
    print("yra 2 skaiciai")
else:
    print("Nera 2 skaiciai")

-----------------------FOR CIKLAS----------------------------------------------
for i in range(1, 11):
    print(i)


vardai = ["Jonas", "Saulius", "Lina", "Marius", "Rugile"]
      # key       value
for vardas in vardai:
    print(vardas)

--------atrinkti skaiciu kurie daugiau nei 25---------------------
skaiciai = [10, 20, 30, 40, 50, 23]
atrinkti=[]

for skaicius in skaiciai:
    if skaicius > 25:
        atrinkti.append(skaicius)
print("Atrinkti skaiciai: ", atrinkti)

-------------------atrinkti nepasikartojancius skaicius is listo--------

skaiciai = [10, 10, 20, 44, 50, 50, 23, 23, 2, 45, 44]
unikalios_reiksmes = []

for skaicius in skaiciai:
        if skaicius not in unikalios_reiksmes:
            unikalios_reiksmes.append(skaicius)
print("Unikalios_reiksmes: ", unikalios_reiksmes)





# ----------------FUNKCIJOS-------------------------------------------!!!!!!!!!!----------------

def suma(a, b):
    return a + b
rezulatatas = suma(2, 5)
print("Suma: ", rezulatatas)


def pasisveikinimas(vardas="Anonimas"):
    print("Labas," , vardas)
pasisveikinimas("Egidijus")


def sujungti_sarasus(sarasas1, sarasas2):
    sujungtas_sarasas = sarasas1 + sarasas2
    return sujungtas_sarasas
sarasas1 = [1, 2, 3]
sarasas2 = [4, 5, 6]
rezultatas = sujungti_sarasus(sarasas1, sarasas2)
print("Sujungtas sarasas: ", rezultatas)

4.Parašykite funkciją ar_lyginis, kuri priima vieną skaičių kaip argumentą ir patikrina, ar skaičius yra lyginis.
Jei skaičius yra lyginis, tada funkcija turi grąžinti True, o jei nelyginis - False.

def ar_lyginis(skaicius):
    if skaicius %2 == 0:
        return True
    else:
        return False
print(ar_lyginis(9))

5. Parašykite funkciją didziausias_skaicius, kuri priima sąrašą skaičių ir grąžina didžiausią skaičių iš sąrašo;
def didziausias_skaicius(sarasas):
    didziausias = sarasas[0]
    for skaicius in sarasas:
        if skaicius > didziausias:
            didziausias = skaicius
    return didziausias
skaiciusarasas = [1, 15, 7, 26, 8, 44, 69, 13, 88, 2]
rezultatas = didziausias_skaicius(skaiciusarasas)
print(rezultatas)
#
6. Parašykite funkciją unikalios_reiksmes,
kuri priima sąrašą ir grąžina naują sąrašą, kuriame yra tik unikalios reikšmės iš pradinio sąrašo

def unikalios_reiksmes(sarasas):
    tuscias_sarasas = []
    for reiksme in sarasas:
        if reiksme not in tuscias_sarasas:
            tuscias_sarasas.append(reiksme)

    return tuscias_sarasas
naujas_sarasas = [1, 25, 36, 2, 0, 88, 102, 88, 13, 88]
print(unikalios_reiksmes(naujas_sarasas))

--------------------------------------18 paskaita----------------------------------

1.Apskaičiuokite skaičių sąrašo suma, išskyrus tuos skaičius, kurie yra lyginiai.
Parašykite funkciją, kuri priima skaičių sąrašą kaip argumentą ir grąžina sumą.

pradinis_sarasas = []

2.Raskite didžiausią skaičių iš Jūsų sukurto skaičių sąrašo.
Parašykite funkciją, kuri priima skaičių sąrašą kaip argumentą ir grąžina didžiausią skaičių.



3.Parašykite funkciją, kuri priima skaičių ir patikrina, ar jis yra pirminis skaičius.

def pirminis_skaicius (skaicius):
    if skaicius < 2:
        return False
    for daliklis in range (2, skaicius):
        if skaicius % daliklis == 0:
            return False
        return True
skaicius = 5
if pirminis_skaicius(skaicius):
    print(f"skaicius {skaicius} yra pirminis skaicius")
else:
    print(f"skaicius{skaicius} yra ne pirminis skaicius")

06.13-------------------DAROM PROGRAMELE----------OBJEKTINIS PROGRAMAVIMAS-------------------18 PASKAITA------------
WHILE

skaicius = 1
while skaicius <= 5:
    print(skaicius)
    skaicius += 1

paparsyti vartotojo ivesti skaiciu ir atsspausdinti ivestus skaiciu lyginius ir atspausdinti mazejimo tvarka

skaicius = int(input("Iveskite skaiciu: "))
while skaicius >= 0:
    if skaicius % 2 == 0:
        print(skaicius)
    skaicius -= 1

--------------------------------OBJEKTINIS PROGRAMAVIMAS-----------





