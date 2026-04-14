"""# Sual 1
tuple = (4,6,3,9,12,24,24,76,63)
indexes = []
index = 0
for i in tuple:
    if i == 24:
        indexes.append(index)
    index += 1
print(f"24 ededinin indexleri: {indexes}")

# Sual 2
tuple = (4,6,3,9,12,24,24,76,63)
for i in tuple:
    if i%3==0:
        print(i,end=" ")

# Sual 3
list1 = []
for i in range(1,6):
    x = int(input(f"{i}. "))
    list1.append(x)
list2 = []
for i in list1:
    list2.append(i+5)
print(list1, list2, sep='\n')

# Sual 4
list1 = []
for i in range(1,6):
    x = int(input(f"{i}. "))
    list1.append(x)
list2 = []
for i in list1:
    if i%2 != 0:
        list2.append(i)
print(list1, list2, sep='\n')

# Sual 5
import random
list = [random.randint(0, 10) for i in range(7)]
cem=0
for i in list:
    cem += i
hasil=1
for i in list:
    hasil*=i
average=cem/7
maximum=0
index=0
for i in list:
    if i > maximum:
        maximum = i
        max_index = index
    index += 1
minimum=11
index=0
for i in list:
    if i < minimum:
        minimum = i
        min_index = index
    index += 1
print(list, cem, hasil, average, maximum, max_index, minimum, min_index, sep="\n")
"""