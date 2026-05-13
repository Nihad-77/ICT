"""# Sual 1
x = float(input("x-i daxil edin: "))
y = float(input("y-i daxil edin: "))

        # Cevrenin sag hissesi olsun, y=x+1 xettinin ustu istisna olmaqla 
if (x >= 0 and x**2+y**2 <= 20) and not y>x+1:
    print(f"({x:.2f},{y:.2f}) nöqtəsi oblasta daxildir!")
else:
    print(f"({x:.2f},{y:.2f}) nöqtəsi oblasta daxil deyil!")
        # Qeyd: cosinus funksiyasinin rolu yoxdur
"""
"""
# Sual 2
n = int(input("Neçə ədəd daxil edəcəksiniz? "))

for i in range(1, n+1):
    eded = int(input(f"{i}-ci ədədi daxil edin: "))
    sum = 0
    if eded <= 0:
        print("(Ədəd uyğun deyil! Proses dayandırılır.)")
        break
    else:
        cut_sayi = 0
        print("(",end="")
        for j in range(2, eded):
            if eded % j == 0 and j % 2 == 0:
                cut_sayi += 1
                if cut_sayi == 1:
                    print(j,end="")
                else:
                    print("+",j,sep="",end="")
                sum += j
        if cut_sayi != 0:
            print(" =", sum, end=")\n\n")
        else:
            print("Cut boleni yoxdur, cem = 0",end=")\n\n")
"""
"""
# Sual 3
eded = int(input("Ededi daxil edin: "))

hasil = eded
addim = 1
while hasil >= 10:
    eded = hasil
    hasil = 1
    print(f"Addim {addim}: ",end="")
    reqem_sayi = 0
    while eded > 0:
        reqem = eded % 10
        eded //= 10
        hasil *= reqem
        reqem_sayi += 1
        if reqem_sayi == 1:
            print(f"{reqem}",end="")
        else:
            print(" *",reqem,end="")
    print(" = ", hasil)
    addim += 1

print("Yekun netice:", hasil)
print("Cemi addim sayi:", addim)
"""
"""
# Sual 4
start = int(input("Start-i daxil edin: "))
end = int(input("End daxil edin: "))
print("Guclu ededler:") #sum of factorials of digits equals itself
for i in range(start, end+1):
    sum_of_factorials = 0
    temp = i
    while temp > 0:
        digit = temp % 10
        factorial = 1
        for j in range(1, digit+1):
            factorial *= j
        temp //= 10
        sum_of_factorials += factorial
    if sum_of_factorials == i:
        print(i)
"""

# Sual 5
def reqem_cemi(N):
    cem = 0
    while N > 0:
        cem += N % 10
        N //= 10
    return cem

def convert_binary(N):
    exponent = 0
    result = 0
    while N > 0:
        remainder = N % 2
        result += remainder*10**exponent
        N //= 2
        exponent += 1
    return result

def count_ones(N):
    count = 0
    while N > 0:
        if N % 10 == 1:
            count += 1
        N //= 10
    return count

start = int(input("Start-i daxil edin: "))
end = int(input("End-i daxil edin: "))
print('Uygun ededler:')
for i in range(start, end+1):
    if reqem_cemi(i) % 2 == 0 and count_ones(convert_binary(i)) % 2 == 0:
        print(i)
