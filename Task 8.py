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

for i in range(length):
    for y in range(0, length-1):
        if yeni_massiv[y] < yeni_massiv[y+1]:
            yeni_massiv[y], yeni_massiv[y+1] = yeni_massiv[y+1], yeni_massiv[y]
print('sorted =',yeni_massiv)

# Sual 3
massiv = []
print("5 setri daxil edin: ")   # Numune: 1.ana \n 2.ata
for i in range(5):
    massiv.append(input().split('.')[-1])
print(massiv)

for i in range(5):
    for x in range(0, len(massiv)-1):
        if massiv[x] > massiv[x+1]:
            massiv[x], massiv[x+1] = massiv[x+1], massiv[x]
print(massiv)

# Sual 4
names = []
print("Ad, ata adi ve soyadinizi daxil edin: ")
print("Numune: A.Q. Veliyev")
print("Bitirmek ucun bos setir daxil et.")
while len(names) < 20:
    name = input()
    if name != "":
        names.append(name)
    else:
        break

def split(x,y): # x = Cumle, y = ayirici
    ifade = ""
    result = []
    index = 0
    while index < len(x):
        if x[index:index+len(y)] == y:
            result.append(ifade)
            ifade = ""
            index += len(y)
        else:
            ifade += x[index]
            index += 1
    result.append(ifade)
    return result

def len(x):
    l = 0
    for _ in x:
        l += 1
    return l

for _ in range(len(names)):
    for x in range(0, len(names) - 1):
        if split(names[x], '. ')[-1] > split(names[x+1], '. ')[-1]:
            names[x], names[x+1] = names[x+1], names[x]
print(names)

# Sual 5
import random
Unsorted = [random.randint(-100, 100) for _ in range(10)]
print('Unsorted =', Unsorted)
for i in range(len(Unsorted)):
    for j in range(0, len(Unsorted)-1):
        if Unsorted[j] < Unsorted[j+1]:
            Unsorted[j], Unsorted[j+1] = Unsorted[j+1], Unsorted[j]
print('Sorted_1 =', Unsorted)
Half1 = Unsorted[:len(Unsorted)//2]
Half2 = Unsorted[len(Unsorted)//2:]
for i in range(len(Half1)):
    for j in range(0, len(Half1)-1):
        if Half1[j] > Half1[j+1]:
            Half1[j], Half1[j+1] = Half1[j+1], Half1[j]
for i in range(len(Half2)):
    for j in range(0, len(Half2)-1):
        if Half2[j] > Half2[j+1]:
            Half2[j], Half2[j+1] = Half2[j+1], Half2[j]
print("Sorted_2 =", Half1+Half2)
"""