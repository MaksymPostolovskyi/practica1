number = 1
culture = input("Введіть культуру: ")
plan = input("Введіть план: ")
fact = input("Введіть факт: ")
percent = int(input("Введіть процент: "))

print("-" * 41)
print(f"|{'N':<8}|{'С/г культура':<15}|{'План':<5}|{'Факт':<4}|{'%':<4}")
print(f"|{number:<8}|{culture:<15}|{plan:<5}|{fact:<4}|{percent:<4}")
print("-" * 41)