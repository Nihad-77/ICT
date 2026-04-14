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

# Sual 6
import random
list1 = [random.randint(1, 100) for i in range(10)]
list2 = []
list3 = []
for i in list1:
    if i < 50:
        list2.append(i)
    else:
        list3.append(i)
sum_list2 = 0
count2 = 0
sum_list3 = 0
count3 = 0
for i in list2:
    sum_list2 += i
    count2 += 1
for i in list3:
    sum_list3 += i
    count3 += 1
print(list1)
print(f"[0, 50) araliginda ededi orta = {(sum_list2/count2):.1f}")
print(f"[50, 100) araliginda ededi orta = {(sum_list3/count3):.1f}")
   
# Sual 7
list = [x**2 for x in range(1, 16)]
y = 0
list2 = []
list3 = []
for i in list:
    if y<=4:
        list2.append(i)
    elif y>=10:
        list3.append(i)
    y += 1
print(list, list2, list3)
"""



   