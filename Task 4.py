'''# Sual 1
x = 5
while x != 11:
    if x != 7 and x != 9:
        print(x)
    x += 1

#Sual 2
x = 0
while True:
    a = float(input("Ededi daxil edin: "))
    if a == 0:
        break
    else:
        x = x + a
print(x)

# Sual 3
x = 0
count = 0
while True:
    a = float(input("Ededi daxil edin: "))
    if a == -1:
        break
    else:
        x = x + a
        count = count + 1
print(x/count)

# Sual 4
N = int(input("Natural eded daxil edin: "))
total = 0
while N > 0:
    digit = N % 10
    N = N // 10
    total = total + digit
print(total)

# Sual 5
n = int(input("Eded daxil edin: "))
original = n
reverse = 0
while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10
if original == reverse:
    print("Beli. Palindromdur.")
else:
    print("Xeyr. Palindrom deyil.")

# Sual 6
n = int(input("Eded daxil edin: "))
eynilik = False
right_digit = n % 10
n = n // 10

while n > 0:
    left_digit = n % 10
    n = n//10
    if left_digit == right_digit:
        eynilik = True
        break
    right_digit = left_digit

if eynilik:
    print("Hə.")
else:
    print("Yox.")

# Sual 7
n = 100
while n != 1000:
    total = 0
    z = n
    d = 3
    while d > 0:
        digit = z % 10
        z = z // 10
        total = total + digit ** 3
        d -= 1
    if total == n:
        print(n)
    n += 1

# Sual 8
n = int(input("n-i daxil edin: "))
p = 2   # ilkin sade bolen
while n > 1:
    if n % p == 0:
        print(p)
        n = n / p
    else:
        p += 1

# Sual 9
n = int(input("ikilik sistemde ededi yazin: "))
x = 0
result = 0
while n > 0:
    digit = n % 10
    n = n // 10
    result = result + digit*2**x
    x += 1
print(result)

# Sual 10
n = int(input("10-luq ədədi daxil edin: "))
binary = 0
mertebe = 1
while n > 0:
    remainder = n % 2
    binary += remainder * mertebe
    mertebe *= 10
    n = n // 2
print(binary)

# Sual 11
x = 0   # Fibonacci = 0,1,1,2,3,5,8,13,21,34,55,89...
n1 = 0
n2 = 1
print('0, 1', end=", ")
while x != 49:  # ededlerin ikisi onsuzda qeyd edilib (geriye 48 eded qalir)
    n2, n1 = n2 + n1, n2
    print(n2, end=", ")
    x += 1

# Sual 12
# a)
total = 0
N = int(input("N-i daxil edin: "))
n = 0
while n != N+1:
    expression = n/(1+n**3)**(1/2)
    total += expression
    n += 1
print(total)
# b)
total = 0
N = int(input("N-i daxil edin: "))
n = 1
while n != N+1:
    expression = n**n/n
    total += expression
    n += 1
print(total)
# c)
total = 0
N = int(input("N-i daxil edin: "))
n = 1
while n != N+1:
    expression = (1.1**n + n**2)/5*n
    total += expression
    n += 1
print(total)

# Sual 13
print("1.) Reqemleri topla\n"
      "2.) Reqemlri vur\n"
      "3.) Cixmaq ucun her hansi bir duymeye bas")
while True:
    n = int(input("2 reqemli eded daxil edin: "))
    m = int(input("Bir secim edin: "))
    if m == 1:
        print(n//10 + n % 10)
    elif m == 2:
        print((n//10) * (n % 10))
    else:
        exit()  # qeyd: sualdakı pencere ancaq IDLE-da açılır.
                # kodu IDLE-da işə salın

# Sual 14
n = int(input("Eded daxil edin: "))
x = 1
while x <= n:
    # Ededin reqemlerini sayaq
    temp = x
    count = 0
    while temp > 0:
        temp = temp // 10
        count += 1
    # Son reqemlerinden eded duzeldek
    square = x*x
    eded = square % (10 ** count)
    if x == eded:
        print("Şərti ödəyən ədədlər")
        print(f"{x}*{x}={square}")
    x += 1

# Sual 15
N = int(input("N-i daxil edin: "))
x = 1
while x <= N:
    temp = x
    bolunme = True  # defolt olaraq bolunur goturek
    while temp >= 1:
        digit = temp % 10
        temp = temp // 10
        if digit > 0:
            if x % digit != 0:
                bolunme = False
                break
        else:
            bolunme = False
    if bolunme:
        print(x, end=" ")
    x += 1
'''
