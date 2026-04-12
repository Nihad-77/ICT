#Sual 1
a = 2 ** 4
print(a)


#Sual 2
width = float(input("Enini daxil edin: \n"))
length = float(input("Uzunlugu daxil edin: \n"))
area = width * length
print(area)


#Sual 3
a = float(input("eni daxil edin: \n"))
b = float(input("uzunlugu daxil edin: \n"))
c = float(input("qalinligi daxil edin: \n"))

V = a * b * c
S = 2 * (a * b + b * c + a * c)
print(V)
print(S)


#Sual 4
import math

r = float(input("radiusu daxil edin: \n"))
h = float(input("hundurluyu daxil edin: \n"))

S = math.pi * (r ** 2) * h
print(S)


#Sual 5
import math
a = 25
b = 17
y = 30
S = 0.5 * a * b * math.sin(math.pi/6)
print(round(S, 2))


#Sual 6
a = int(input("Eded daxil edin"))
b = int(input("Eded daxil edin"))
c = int(input("Eded daxil edin"))

print(a+b+c)
print(a*b*c)
print((a+b+c)/3)


#Sual 7
import random
a = str(random.randint(1000, 9999))
print(a)
print(int(a[0])**2 + int(a[1])**2 + int(a[2])**2 + int(a[3])**2)
print(int(a[0])*int(a[1])*int(a[2])*int(a[3]))


#Sual 8
import random
a = random.uniform(6.5, 10.5)
b = random.uniform(6.5, 10.5)
print(round((a * b), 2))


#Sual 9
import random
a = str(random.randint(10000, 99999))
a1 = int(a[0])
a2 = int(a[1])
a3 = int(a[2])
a4 = int(a[3])
print(a1, a1 ** 2)
print(a2, a2 ** 2)
print(a3, a3 ** 2)
print(a4, a4 ** 2)


#Sual 10
import random
import math
x = random.uniform(-1, 1)
y = random.uniform(-1, 1)
a = (math.sqrt(1 + y ** 2)) * math.sin(x**2/(1 + abs(y)))
b = math.cos((math.sin(5 * x)**2)/math.sqrt(abs(y)))
print(round(a, 3), round(b, 3))


#Sual 11
a = int(input("Eded daxil edin: \n"))
print(str(a//100) + ',' + str((a//10)%10) + ',' + str(a%10))
