"""# Sual 1
a = float(input("Eded daxil edin: "))
b = float(input("Eded daxil edin: "))

if a > b:
    print("Boyuk eded: ", a)
else:
    print("Boyuk eded: ", b)

# Sual 2
a = float(input("Eded daxil edin: "))
if a > 0:
    print(a, " musbetdir.")
elif a < 0:
    print(a, " menfidir.")
else:
    print(a, " 0-dir.")

# Sual 3
name = input("Enter thy name: ")
grade1 = float(input("Register thy first score: "))
grade2 = float(input("Enter thy second score: "))
grade3 = float(input("And the last score: "))
mark = (grade1+grade2+grade3)/3
print(name, mark)
if mark >= 85:
    print("Excellent")
elif 75 <= mark < 85:
    print("Very Good")
elif 65 <= mark < 75:
    print("Good")
elif 50 <= mark < 65:
    print("Pass")
else:
    print("Fail")

# Sual 4
a = int(input('Eded daxil edin: '))
if a % 3 == 0:
    print("Eded 3-e bolunur.")
else:
    print("Eded 3-e bolunmur.")

# Sual 5
a = int(input('Eded daxil edin: '))
if a % 6 == 0:
    print("Eded 6-ya bolunur.")
else:
    print("Eded 6-ya bolunmur.")

# Sual 6
a = int(input("Eded daxil edin: "))
if a % 2 == 0:
    print("Eded cutdur.")
else:
    print("Eded tekdir.")

# Sual 7
a = float(input("1-ci ededi daxil edin: "))
b = float(input("2-ci ededi daxil edin: "))
c = float(input("3-cu ededi daxil edin: "))

if a == b == c:
    print((a+b+c)*3)
else:
    print(a+b+c)

# Sual 8
a = float(input("1-ci ededi daxil edin: "))
b = float(input("2-ci ededi daxil edin: "))
c = float(input("3-cu ededi daxil edin: "))

if a == b or b == c or a == c:
    print(0)
else:
    print(a+b+c)

# Sual 9
import math
a = float(input("Tenliyin a-sini daxil edin: "))
b = float(input("Tenliyin b-sini daxil edin: "))
c = float(input("Tenliyin c-sini daxil edin: "))
D = b**2 - 4*a*c    # Diskriminant
if D > 0 or D == 0:
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)

if D > 0:
    print("Tenliyin iki heqiqi koku var")
    print(str(x1) + ", " + str(x2))
elif D == 0:
    print("Tenliyin bir heqiqi koku var")
    print(str(x1))
else:
    print("Tenliyin koku yoxdur")

# Sual 10
ilkin_qiymet = float(input("Qiymeti daxil edin: "))

if ilkin_qiymet < 1000:
    endirim = float(input("Endirimi daxil edin: "))
    qiymet = ilkin_qiymet - ilkin_qiymet * endirim / 100
    print(qiymet)
else:
    qiymet = ilkin_qiymet * 0.9
    print(qiymet)

# Sual 11
ilkin_qiymet = float(input("Qiymeti daxil edin: "))

if ilkin_qiymet <= 500:
    endirim = float(input("Endirimi daxil edin: "))
    qiymet = ilkin_qiymet - ilkin_qiymet * endirim / 100
    print(qiymet)
elif ilkin_qiymet > 1000:
    qiymet = ilkin_qiymet * 0.95
    print(qiymet)
else:
    qiymet = ilkin_qiymet * 0.97
    print(qiymet)

# Sual 12
a = float(input("1-ci ededi daxil edin: "))
b = float(input("2-ci ededi daxil edin: "))

if a > b:
    print(str(a) + " boyukdur " + str(b) + "-den.")
elif a < b:
    print(str(a) + " kicikdir " + str(b) + "-den.")
else:
    print(str(a) + " beraberdir " + str(b) + ".")

# Sual 13
import random
a = random.uniform(0, 100)
b = random.uniform(0, 100)
c = random.uniform(0, 100)
print(a, b, c)
if a < b < c or c < b < a:
    print("Median:", b)
elif a < c < b or b < c <a:
    print("Median:", c)
else:
    print("Median:", a)

# Sual 14
names = {3: "Triangle",
         4: "Quadrilateral",
         5: "Pentagon",
         6: "Hexagon",
         7: "Heptagon",
         8: "Octagon",
         9: "Nonagon",
         10: "Decagon"
         }
sides = int(input("Tereflerin sayini daxil edin: "))
print(names.get(sides, "3-10 arasi tam eded daxil edin"))

# Sual 15
days = {"Yanvar": "31 gun",
        "Fevral": "28 gun ve ya 29 gun",
        "Mart": "31 gun",
        "Aprel": "30 gun",
        "May": "31 gun",
        "Iyun": "30 gun",
        "Iyul": "31 gun",
        "Avqust": "31 gun",
        "Sentyabr": "30 gun",
        "Oktyabr": "31 gun",
        "Noyabr": "30 gun",
        "Dekabr": "31 gun"}

ay = input("Ayi daxil edin: ")
print(days[ay.capitalize()])

# Sual 16:
asif = int(input("Asifin yasini qeyd edin: "))
vasif = int(input("Vasifin yasini qeyd edin: "))
agasif = int(input("Agasifin yasini qeyd edin: "))


def ages():
    print("Asifin yasi:", asif)
    print("Vasifin yasi:", vasif)
    print("Agasifin yasi:", agasif)


if asif == vasif > agasif:
    ages()
    print("Cavab: Asif ve Vasif yasca Agasifden boyukdurler.")
elif asif == agasif > vasif:
    ages()
    print("Cavab: Asif ve Agasif yasca Vasifden boyukdurler.")
elif vasif == agasif > asif:
    ages()
    print("Cavab: Vasif ve Agasif yasca Asifden boyukdurler.")
elif asif == vasif == agasif:
    ages()
    print("Cavab: Asif, Vasif, ve Agasif yasca beraberdir.")
elif asif > vasif and asif > agasif:
    ages()
    print("Cavab: Asif hamidan yasca boyukdur.")
elif vasif > asif and vasif > agasif:
    ages()
    print("Cavab: Vasif hamidan yasca boyukdur.")
else:
    ages()
    print("Cavab: Agasif hamidan yasca boyukdur.")


# Sual 17
a = float(input("1-ci terefi daxil edin: "))
b = float(input("2-ci terefi daxil edin: "))
c = float(input("3-cu terefi daxil edin: "))

if a == b == c:
    print("Berabertereflidir.")
elif a == b or a == c or b == c:
    print("Beraberyanlidir.")
else:
    print("Müxteliftereflidir.")

# Sual 18
db = float(input("Sesin seviyyesini daxil edin: "))
if db > 130:
    print("Maksimal qiymetden boyukdur (Jackhammer).")
elif db == 130:
    print("Jackhammer")
elif 106 < db < 130:
    print("Gas lawnmower - Jackhammer")
elif db == 106:
    print("Gas lawnmower")
elif 70 < db < 106:
    print("Alarm clock - Gas lawnmower")
elif db == 70:
    print("Alarm clock")
elif 40 < db < 70:
    print("Quiet room - Alarm clock")
elif db == 40:
    print("Quiet room")
else:
    print("Minimal qiymetden kicikdir (Quiet room).")

# Sual 19
il = int(input("Ili daxil edin: "))
if il % 400 == 0:
    print(il, "uzun ildir.")
elif il % 100 == 0:
    print(il, "uzun il deyil.")
elif il % 4 == 0:
    print(il, "uzun ildir.")
else:
    print(il, "uzun il deyil.")

# Sual 20:
magnitude = float(input("Enter the magnitude: "))
if magnitude < 2.0:
    print("Micro")
elif 2.0 <= magnitude < 3.0:
    print("Very minor")
elif 3.0 <= magnitude < 4.0:
    print("Minor")
elif 4.0 <= magnitude < 5.0:
    print("Light")
elif 5.0 <= magnitude < 6.0:
    print("Moderate")
elif 6.0 <= magnitude < 7.0:
    print("Strong")
elif 7.0 <= magnitude < 8.0:
    print("Major")
elif 8.0 <= magnitude < 10.0:
    print("Great")
else:
    print("Meteoric")

# Sual 21
legal_rows = ['1', '2', '3', '4', '5', '6', '7', '8']
legal_columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

while True:
    coordinate = input("Koordinati daxil edin: ")
    row = coordinate[1]
    column = coordinate[0]
    if row not in legal_rows or column not in legal_columns:
        print("a1-h8 arasi secin.")
        continue
    break

row_index = legal_rows.index(row)
column_index = legal_columns.index(column)

x = row_index % 2
y = column_index % 2

if x == 0 and y == 0 or x == 1 and y == 1:
    print("Xana Qaradir")
else:
    print("Xana Agdir")

# Sual 22
# A)
x = float(input("x-i daxil edin: "))
y = float(input("y-i daxil edin: "))
if y >= x**2 - 2 and (abs(x) >= abs(y)):
    print("Daxil")
else:
    print("Daxil deyil")

# B)
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
"""