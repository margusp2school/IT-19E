# https://www.w3schools.com/python/python_conditions.asp
numbrid = []

# 1. Küsida, mitu vanust tahad sisestada
# 2. Nende vanuste keskmine välja printida

mitu_vanust = int(input("Mitu vanust soovid sisestada?: "))

for i in range(0, mitu_vanust):
    number = int(input("Number " + str(i) + ": "))
    numbrid.append(number)

summa = 0
for x in numbrid:
    summa = summa + x 
print(summa / mitu_vanust)


# Ülesanded
# 1. Prindi välja kõige suurem number
# 2. Prindi välja kõige väiksem number
# Kasuta abiks: https://www.w3schools.com/python/python_conditions.asp


# Summa
# summa = 0
# for x in numbrid:
#     summa = summa + x 
# print(summa)

# k6ige_suurem_number = 0
# for x in numbrid:
#     if x > k6ige_suurem_number:
#         k6ige_suurem_number = x 
# print(k6ige_suurem_number)