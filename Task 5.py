"""# Sual 1
def toplama():
    x = int(input("Eded daxil edin: "))
    while x != -1:
        if x % 2 == 0:
            print("Cutdur")
        else:
            print("Tekdir")
        x = int(input("Eded daxil edin: "))

# Sual 2
def funksiya(a, b):
    if (a / b) % 2 == 0:
        print(True)
    else:
        print(False)
a = int(input("a-ni daxil edin: "))
b = int(input("b-ni daxil edin: "))
funksiya(a, b)

#Sual 3
def funksiya(n, k):
    if k ** k == n:
        print(True)
    else:
        print(False)
k = int(input("k-ni daxil edin: "))
n = int(input("n-i daxil edin: "))
funksiya(n, k)

# Sual 4
def pronic(p):
    n = 0
    while n * (n + 1) <= p:
        if n * (n + 1) == p:
            print("Pronic")
            return
        n += 1
    print("Heteromecic")

p = int(input("Eded daxil edin: "))
pronic(p)


# Sual 5
def uzunluq(a):
    if a == 0:
        print(1)
    elif a < 0:
        a = -a
        count = 0
        while a > 0:
            a //= 10
            count += 1
        print(count)
    else:
        count = 0
        while a > 0:
            a //= 10
            count += 1
        print(count)
a = int(input("Eded daxil edin: "))
uzunluq(a)

# Sual 6
def Disarium(N):
    total = 0
    exponent = 0
    temp = N
    while temp > 0:
        temp //= 10
        exponent += 1
    temp = N
    while temp > 0:
        digit = temp % 10
        temp //= 10
        total += digit ** exponent
        exponent -= 1
    if total == N:
        print("Disarium ededdir.")
    else:
        print("Disarium eded deyil")

Disarium(int(input("N ededi daxil edin: ")))

# Sual 7
def Curzon(N):
    if (2**N+1) % (2*N+1) == 0:
        print("Curzon ededdir.")
    else:
        print("Curzon eded deyil.")

Curzon(int(input("N ededi daxil edin: ")))

# Sual 8
def Kempner(N):
    # meselen 8 daxil olunubsa en kicik 4 dur cunki ancaq onun faktorialina bolunur
    n = 1
    while True:
        factorial = 1
        m = 1
        while m <= n:
            factorial *= m
            m += 1
        if factorial % N == 0:
            return print(n, "!", sep="")
        n += 1
Kempner(int(input("Eded gir: ")))

# Sual 9
def sadelik(n):
    if n < 2:
        return False
    i = 2
    while i <= n-1:     # proqramin suretini artirmaq ucun i*i <= n yazmaqda olar amma kecmemisik
        if n % i == 0:
            return False
        i += 1
    return True


def Moran(N):
    temp = N
    digit_sum = 0

    # Sum of digits
    while temp > 0:
        digit_sum += temp % 10
        temp //= 10

    if digit_sum == 0:
        print("Moran deyil")
        return

    if N % digit_sum == 0:
        qismet = N // digit_sum
        if sadelik(qismet):
            print("Moran ededdir")
            return

    print("Moran deyil")


N = int(input("Eded daxil edin: "))
Moran(N)

# Sual 10-11 (Taskda sual 10 ve 11 bir-birine qarisib, eyni sualdir)
def funksiya(N):
    son_reqem = N % 10
    temp = N
    while temp >= 10:
        temp //= 10
    ilk_reqem = temp
    if (ilk_reqem + son_reqem)**0.5 > 3:
        return print(True)
    return print(False)
funksiya(int(input("Eded daxil edin: ")))

# Sual 12
    # qasiliqli sade = EBOB(a,b) = 1 'coprime' adlanir ingilisce
def coprime(a,b):
    while b != 0:
        a, b = b, a % b  # Evklid usulu
    if a == 1:
        print(True)
    else:
        print(False)
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
coprime(a,b)

# Sual 13
def hyper_primality(N):
    x = 2
    prime = True
    while x < N:
        if N % x == 0:
            prime = False
            break
        else:
            x = x + 1

    if N > 99:
        n = N // 10    # son reqemi sil
        power = 1
        while power * 10 <= n:
            power *= 10
        n -= (n // power) * power   # ilk reqemi sil

        y = 2
        prime2 = True
        while y < n:
            if n % y == 0:
                prime2 = False
                break
            else:
                y = y + 1

        if prime and prime2:
            print(N, "hyperprime ededdir.")
        else:
            print(N, "hyperprime deyil.")
    else:
        print(N, "hyperprime eded ola bilmez.")



hyper_primality(int(input("Enter your number: ")))

# Sual 14
def EBOB(a, b):
    while b != 0:
        a, b = b, a % b     # Evklid usulu
    return a

def EKOB(a, b):
    return (a * b) // EBOB(a, b)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(f"EBOB = {EBOB(a, b)}")  #
print(f"EKOB = {EKOB(a, b)}")  #

# Sual 15
def sort(a, b, c):
    if a > b:
        a, b = b, a
    if b > c:
        b, c = c, b
    if a > b:
        a, b = b, a
    return a, b, c

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
print(sort(a, b, c))

# Sual 16
def simplify(suret, mexrec):
    # EBOB tapib suret ve mexreci ona bolmeliyik.
    def EBOB(a, b):
        while b != 0:
            a, b = b, a % b
        return a
    ebob = EBOB(suret, mexrec)
    suret = int(suret/ebob)
    mexrec = int(mexrec/ebob)
    return f"{suret}/{mexrec}"

M = int(input("Enter M: "))
N = int(input("Enter N: "))

print(simplify(M, N))

def reverse(n):
    result = 0
    while n > 0:
        result = result * 10 + n % 10
        n //= 10
    return result

print(reverse(12345))  # 54321
"""