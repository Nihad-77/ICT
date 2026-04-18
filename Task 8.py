"""# Sual 1
import random
massiv = [random.randint(0,5) for _ in range(random.randint(5,10)]
print(massiv)
find = int(input("Ne axtaririq: "))
tapilanlar = []
index = 0
for element in massiv:
    if element == find:
        tapilanlar.append(f"A[{index}]={element}")
    index += 1
if tapilanlar:
    print("Tapildi: ")
    for i in tapilanlar:
        print(i,end=", ")
else:
    print("Tapilmadi.")

# Sual 2
import random

def sum_of_digits(x):
    sum = 0
    while x > 0:
        sum += x % 10
        x //= 10
    return sum

massiv = [random.randint(10, 100) for _ in range(random.randint(5,15))]
print('massiv =',massiv)
yeni_massiv = []

for i in massiv:
    yeni_massiv.append(sum_of_digits(i))

print('reqemleri toplanmis =',yeni_massiv)

length = 0
for i in yeni_massiv:
    length+=1

for x in range(length):
    for y in range(0, length-1):
        if yeni_massiv[y] < yeni_massiv[y+1]:
            yeni_massiv[y], yeni_massiv[y+1] = yeni_massiv[y+1], yeni_massiv[y]
print('sorted =',yeni_massiv)
"""
