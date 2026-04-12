'''x = float(input("x-i daxil edin: "))
y = float(input("y-i daxil edin: "))
if (x <= 0 and x**2 + y**2 <= 25) and not (x > -2  0 < y < x + 2):
    print("Daxildir")
else:
    print("Daxil deyil")


x = float(input("x-i daxil edin: "))
y = float(input("y-i daxil edin: "))
if (x**2 + y**2 <= 1) and not (y < x and not (y < 0 and x < 0)):
    print("Daxil")
else:
    print('Daxil deyil')

# C)
x = float(input("x-i daxil edin: "))
y = float(input("y-i daxil edin: "))
if x**2 + y**2 <= 1 and not (y > x and not abs(y) > abs(x)):
    print("Daxildir.")
else:
    print("Daxil deyil.")

# D)
x = float(input("x-i daxil edin: "))
y = float(input("y-i daxil edin: "))
if y >= 2*x**2 and y >= 1 - x and x <= 1:
    print("Daxildir.")
else:
    print("Daxil deyil.")

# E)
x = float(input("x-i daxil edin: "))
y = float(input("y-i daxil edin: "))
if x >= 0 and ((x**2 + y**2 <= 1) or (1 >= y >= x - 1)):
    print("Daxildir.")
else:
    print("Daxil deyil.")

# F)
x = float(input("x-i daxil edin: "))
y = float(input("y-i daxil edin: "))
if x**2 + y**2 <= 1 or (0 <= x <= 1 and 0 <= y <= 1):
    print("Daxildir.")
else:
    print("Daxil deyil.")

# G)
x = float(input("x-i daxil edin: "))
y = float(input("y-i daxil edin: "))
try:
    if 1/x <= y <= -x + 4 or -x - 4 <= y <= 1/x:
        print("Daxildir.")
    else:
        print("Daxil deyil.")
except ZeroDivisionError:
    print("Bu nöqtə təyin olunmayıb")


# H)
x = float(input("x-i daxil edin: "))
y = float(input("y-i daxil edin: "))
if x**2 <= y <= 1 or -1 <= y <= -x ** 2:
    print("Daxildir.")
else:
    print("Daxil deyil.")

# J)
x = float(input("x-i daxil edin: "))
y = float(input("y-i daxil edin: "))
if x >= y >= -2 and not x ** 2 + y ** 2 <= 4:
    print("Daxildir.")
else:
    print("Daxil deyil.")

# K)
x = float(input("x-i daxil edin: "))
y = float(input("y-i daxil edin: "))
if y >= (x-2)**2 - 3 and (y >= 0 and x >= abs(y) or y <= 0 and x <= abs(y)):
    print("Daxildir.")
else:
    print("Daxil deyil.")

# L)
x = float(input("x-i daxil edin: "))
y = float(input("y-i daxil edin: "))
if x <= 0 and x**2 + y**2 <= 25 and not (0 < y < 2 and y < x + 2):
    print("Daxildir.")
else:
    print("Daxil deyil.")

# M)
x = float(input("x-i daxil edin: "))
y = float(input("y-i daxil edin: "))
if x**2 + y**2 <= 1 and y <= 1 - x and not (x < 0 and y < 0):
    print("Daxildir.")
else:
    print("Daxil deyil.")

# N)
x = float(input("x-i daxil edin: "))
y = float(input("y-i daxil edin: "))
if (x**2 + y**2 <= 1 and y >= x) or (x >= -1 and y <= 1):
    print("Daxildir.")
else:
    print("Daxil deyil.")




n = 100
while n != 10000000000:
    total = 0
    t = n
    digit_count = 0
    while t > 0:
        digit = t % 10
        t = t // 10
        digit_count += 1
    z = n
    for i in range(digit_count):
        digit = z % 10
        z = z // 10
        total = total + digit**digit_count
    if total == n:
        print(n)
    n += 1
'''
n = int(input("Eded daxil edin: "))
x = 1

while x <= n:
    temp = x
    count = 0

    # Count digits
    while temp > 0:
        temp //= 10
        count += 1

    square = x * x
    last_part = square % (10 ** count)

    if last_part == x:
        print(f"{x} * {x} = {square}")

    x += 1

n = int(input("Eded daxil edin: "))
x = 1

while x <= n:
    temp = x
    count = 0

    while temp > 0:
        temp = temp // 10
        count += 1

    square = x * x
    eded = square % (10 ** count)

    if x == eded:
        print(f"{x}*{x}={square}")

    x += 1
