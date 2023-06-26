
# --------------------------------25 paskaita(06.26)-----------------------------------------------


# employees.csv
#
# 1.Apskaičiuoti vidurkį, sumą, minimumą, maksimumą ir kitus statistinius rodiklius stulpeliuose arba
# grupėse naudojant mean(), sum(), min(), max() ir kitas funkcijas.

# import pandas as pd
# import matplotlib.pyplot as plt
# df = pd.read_csv('employees.csv')
# print(df.head(1))

# import pandas as pd
# from pathlib import Path
# import matplotlib.pyplot as plt
# file_path = Path('employees1.csv')
# df = pd.read_csv(file_path)

# df = pd.DataFrame(data)

# group_average = df.groupby('FIRST_NAME')['DEPARTMENT_ID'].mean()
# print(group_average)
#
# group_sum = df.groupby('FIRST_NAME')['SALARY'].sum()
# print(group_sum)
#
# group_max = df.groupby('FIRST_NAME')['SALARY'].max()
# print(group_max)
#
# group_min = df.groupby('FIRST_NAME')['SALARY'].min()
# print(group_min)

# 2. Grupuoti duomenis pagal tam tikrą stulpelį ir atlikti agregavimo operacijas,
# pvz., apskaičiuoti bendrą sumą ar vidurkį kiekvienai grupės naudojant groupby() funkciją.

# selected_columns = df[['EMPLOYEE_ID', 'SALARY']].mean()
# print(selected_columns)

# *3.Atlikti reikiamus duomenų valymo veiksmus, pvz., pašalinti dublikatus, užpildyti trūkstamas
# reikšmes arba pašalinti netinkamas reikšmes.


