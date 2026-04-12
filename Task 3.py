'''# Sual 1
a = float(input("a-ni daxil edin: "))
x = int(input("x-i daxil edin: "))
result = 1
for i in range(x):
    result = result * a
print(result)


# Sual 2
A = int(input("A-ni daxil edin: "))
result = 1
for i in range(1, A + 1):
    result = result * i
print(result)


# Sual 3
for i in range(1, 51):
    if i % 2 == 0:
        print(i)


# Sual 4
N = int(input("N-i daxil edin: "))
result = 0
for i in range(1, N+1):
    result += i
print(result)


# Sual 5
X = int(input("X-i daxil edin: "))
N = int(input("N-i daxil edin: "))
result = 0
for i in range(0, N+1):
    result = result + X**i
    X = -X
print(result)


# Sual 6
for i in range(100, 0, -1):
    print(i)


# Sual 7
for i in range(0, 11):
    print(i, i**2)


# Sual 8
odds = 1
evens = 0
for i in range(0, 11):
    if i % 2 == 0:
        evens = evens + i
    else:
        odds = odds * i
print("Cutlerin cemi:", evens)
print("Teklerin hasili:", odds)


# Sual 9
A = int(input("A-ni daxil edin: "))
B = int(input("B-ni daxil edin: "))
C = int(input("C-ni daxil edin: "))
for i in range(A, B+1):
    if i % C == 0:
        print(i)


# Sual 10
A = int(input("A-ni daxil edin: "))
B = int(input("B-ni daxil edin: "))
count_even = 0
count_odd = 0
for i in range(A, B+1):
    if i % 2 == 0:
        count_even += 1
    else:
        count_odd += 1
print("Cutlerin sayi:", count_even)
print("Teklerin sayi:", count_odd)


# Sual 11
import random
for i in range(10):
    x = random.randint(1,10)
    if x % 2 == 0:
        print(x, "cutdur.")
    else:
        print(x, "tekdir.")


# Sual 12
A = int(input("A-ni daxil edin: "))
B = int(input("B-ni daxil edin: "))
for i in range(A, B+1):
    print(i*i)


# Sual 13
a = int(input("A-ni daxil edin: "))
b = int(input("B-ni daxil edin: "))
result = 0
for i in range(abs(a)):
    result = result + b
print(result)


# Sual 14
pi = 3
x = 4
for i in range(0, 30, 2):
    pi += x/((i+2)*(i+3)*(i+4))
    x = -x
print(pi)


# Sual 15
for i in range(10000, 100000):
    if i % 133 == 125 and i % 134 == 111:
        print(i)


# Sual 16
A = int(input("A-ni daxil edin: "))
B = int(input("B-ni daxil edin: "))
for i in range(1, b+1):
    if a % i == 0 and b % i == 0:
        EBOB = i
print(EBOB)


# Sual 17
A = int(input("A-ni daxil edin (A<B): "))
B = int(input("B-ni daxil edin (A<B): "))

for x in range(A, B+1):
    sade = True
    for y in range(2, x):
        if x % y == 0:
            sade = False
            break
        else:
            continue
    if sade:
        print(x, 'sadedir.')
    else:
        pass


# Sual 18
count = 0
for x in range(185 // 15 + 1):
    for y in range(185 // 17 + 1):
        for z in range(185 // 21 + 1):
            if 15*x+17*y+21*z == 185:
                count += 1
print(count)'''
