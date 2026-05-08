"""# Sual 1
import random
N = int(input("N-i daxil edin: "))
M = int(input("M-i daxil edin: "))
matrix = [[random.randint(-10,10) for _ in range(N)] for _ in range(M)]
for row in matrix:   # Matrixi daha sade gostermek ucun
    print(row)
# a), b) 
print("a),b)")
mutleq_cem = 0
kvadrat_cem = 0
for row in matrix:
    for i in row:
        mutleq_cem += abs(i)
        kvadrat_cem += i*i
print("Mutleq qiymetler cemi:",mutleq_cem)
print("Kvadratlar cemi:", kvadrat_cem)
# c)
print("c)")
K = int(input("K-setrin daxil et: ")) - 1
hasil = 1
for i in matrix[K]:
    hasil*=i
print(hasil)
# d)
print("d)")
min_idx = 0
min = 11
sum=0
for row in matrix:    # en kicik ededi tapib onun indexin mueyyenlesdirrik
    for y in range(len(row)):
        if row[y] < min:
            min_idx = y
            min = row[y]
for row in matrix:  # her setirden tapdigimiz indexe uygun ededi ustune gellik
    sum+=row[min_idx]
print("en kicik ededli sutunun cemi:",sum)
# e)
print("e)")
left_diagonal = []
right_diagonal = []
idx = 0
for row in matrix:
    left_diagonal += [row[idx]]
    idx +=1
idx = N-1
for row in matrix:
    right_diagonal += [row[idx]]
    idx -= 1
print(left_diagonal,right_diagonal,sep="\n")

# Sual 2
import random
n = int(input("n-i daxil edin: "))
matrix_A = [[random.randint(-10,10) for _ in range(n)] for _ in range(n)]
matrix_B = [[random.randint(-10,10) for _ in range(n)] for _ in range(n)]
print("Matrix A= ",end="")
for row in matrix_A:  # Matrixi daha sade gostermek ucun
    print(row)
print("Matrix B= ",end="")
for row in matrix_B:
    print(row)
# a)
print("a)")
matrix_C = []
for i in range(n):
    row = []
    for j in range(n):
        sum = matrix_A[i][j] + matrix_B[i][j]
        diff = matrix_A[i][j] - matrix_B[i][j]
        row += [(sum, diff)]
    matrix_C += [row]
print("Matrix C= ",end="")
for row in matrix_C:
    print(row)
# b)
print("b)")
k = int(input("k-ni daxil edin: "))
m = int(input("m-i daxil edin: "))
massiv_B = []
row_k = matrix_A[k]
col_m = [row[m] for row in matrix_A]
for i in range(n):
    massiv_B += [row_k[i] * col_m[i]]
print("B massivi=", massiv_B)
# c)
print("c)")
diaqonal_A = []
for i in range(n):
    for j in range(n):
        if i == j:
            diaqonal_A += [matrix_A[i][j]]
for i in range(n):
    massiv_B += [row_k[i] / diaqonal_A[i] if diaqonal_A[i] != 0 else "-"]
print(massiv_B)
# d)
print("d)")
sum = 0
for i in diaqonal_A:
    sum += i
print('sum=',sum)
for i in range(n):
    if i % 2 != 0:
        for j in range(n):
            matrix_A[i][j] = float(f"{(matrix_A[i][j] / sum):.2f}")
print("Yeni Matrix A= ",end="")
for row in matrix_A:
    print(row)
# e)
print("e)")
matrix = [[random.randint(-10, 10) for _ in range(n)] for _ in range(n)]
sum = 0
massiv_setir = []
massiv_sutun = []
print("matrix= ",end="")
for row in matrix:
    print(row)
    for i in row:
        sum += i
    massiv_setir += [sum]
hasil = 1
for i in range(n):
    idx = 0
    for j in range(n):
        if j == idx:
            hasil *= matrix[i][j]
    massiv_sutun += [hasil]
print("Setirler cemi massivi =", massiv_setir)
print("Sutunlar hasili massivi =", massiv_sutun)

# Sual 3
import random
N = int(input("N-i daxil edin: "))
matrix = [[random.randint(10,100) for _ in range(N)] for _ in range(N)]
for row in matrix:
    print(row)
# a)
print("a)")
max = 0
for i in range(N):
    for j in range(N):
        if matrix[i][j] > max:
            max_index = (i,j)
            max = matrix[i][j]
print("Maximum is",max,". Its index is",max_index)
# b)
print("b)")
for i in range(N//2):
    for j in range(N):
        matrix[i][j], matrix[N-1-i][j] = matrix[N-1-i][j], matrix[i][j]
print("Sutunlari cevrilmis matrix= ",end="")
for row in matrix:
    print(row)
# c)
print("c)")
def pronic(x):
    for i in range(x):
        if (i)*(i+1) == x:
            return True
    return False
pronics = []
for i in range(N):
    if i % 2 != 0:
        for j in range(N):
            if pronic(matrix[i][j]):
                pronics += [matrix[i][j]]
print("Pronikler=",pronics)
# d)
print("d)")
primes = []
def prime(x):
    if x < 2:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True
for i in range(N):
    for j in range(N):
        if i == j or i == N-1-j:
            if prime(matrix[i][j]):
                primes += [matrix[i][j]]
print("Primes on diagonal=",primes)

# Sual 4
import random
N = int(input("N-i daxil edin: "))
matrix = [[random.randint(10,99) for _ in range(N)] for _ in range(N)]
for row in matrix:
    print(row)
# a)
print("a)")
sum = 0
for row in matrix:
    for i in row:
        sum += i
average = sum / N**2
for i in range(N):
    for j in range(N):
        if matrix[i][j] < average:
            matrix[i][j] = 0
        else:
            matrix[i][j] = 255
print("Ag qara matrix= ",end="")
for row in matrix:
    print(row)
# b)
print("b)")
matrix = [[random.randint(10,99) for _ in range(N)] for _ in range(N)]
for row in matrix:
    print(row)
print("")
for i in range(N):
    for j in range(N):
        if i < j:   # diaqonaldan yuxari
            if matrix[i][j] > 50:
                matrix[i][j] = 255
            else:
                matrix[i][j] = 0
for row in matrix:
    print(row)
# c)
print("c)")
matrix = [[random.randint(10,99) for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if j >= i:
            matrix[i][j]=0
print("")
for row in matrix:
    print(row)
print("")
# d)
print("d)")
matrix = [[random.randint(10,99) for _ in range(N)] for _ in range(N)]
for row in matrix:
    print(row)
for i in range(N):
    for j in range(N//2):
        matrix[i][j], matrix[i][N-1-j] = matrix[i][N-1-j], matrix[i][j]
print("")
for row in matrix:
    print(row)
# e)
print('e)')
print("SUAL 3-ün b varianti ile eyni oldugu ucun tezden yazmiram.")
# f)
print("f)")
matrix = [[random.randint(10,99) for _ in range(N)] for _ in range(N)]
for row in matrix:
    print(row)
print("")

for i in range(N):
    for j in range(i + 1, N):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
for i in range(N):
    for j in range(N // 2):
        matrix[i][j], matrix[i][N-1-j] = matrix[i][N-1-j], matrix[i][j]
for row in matrix:
    print(row)

# Sual 5
import random
N = int(input("N-i daxil edin: "))
matrix = [[random.randint(10,20) for _ in range(N)] for _ in range(N)]
matrix2 = [row[:] for row in matrix]
matrix3 = [row[:] for row in matrix]
matrix4 = [row[:] for row in matrix]
matrix5 = [row[:] for row in matrix]
matrix6 = [row[:] for row in matrix]
def n_herfi(x, N):
    for i in range(N):
        for j in range(N):
            if j == 0 or j==N-1 or (i == j):
                x[i][j] = "+"
    for row in x:
        print(row)
def a_herfi(x,N):
    for i in range(N):
        for j in range(N):
            if i == 0 or i == 2 or j == 0 or j == N-1:
                x[i][j] = "+"
    for row in x:
        print(row)
def y_herfi(x, N):
    for i in range(N):
        for j in range(N):
            if (i > N//2 and j == N//2) or (i <= N//2 and (i == j or (i == N-1-j))):
                x[i][j] = 0
    for row in x:
        print(row)
def t_herfi(x, N):
    for i in range(N):
        for j in range(N):
            if i == 0 or j == N//2:
                x[i][j] = 0
    for row in x:
        print(row)
def z_herfi(x, N):
    for i in range(N):
        for j in range(N):
            if i == 0 or i == N-1 or j == N-1-i:
                x[i][j] = 0
    for row in x:
        print(row)
def o_herfi(x, N):
    for i in range(N):
        for j in range(N):
            if i == 0 or i == N-1 or j == 0 or j == N-1:
                x[i][j] = "+"
    for row in x:
        print(row) 
    
n_herfi(matrix, N)
print("")
a_herfi(matrix2, N)
print("")
y_herfi(matrix3, N)
print("")
t_herfi(matrix4, N)
print("")
z_herfi(matrix5, N)
print("")
o_herfi(matrix6, N)
"""
"""
### DICTIONARY
# Sual 1
Dict = {	
'Asia':	{ 'population': 4545133094, 'area': 31033131 },
'Africa':	{ 'population': 1287920518, 'area': 29648481 },
'Europe':	{ 'population': 742648010, 'area': 22134900 },
'North America':	{ 'population': 587615976, 'area': 21329926 },
'South America':	{ 'population': 428240515, 'area': 17461112 },
'Australia/Oceania':	{ 'population': 41261212, 'area': 8486460 },
'Antarctica':		{ 'population': 0, 'area': 13720000 }
}
new_list=[]	
for key in Dict:
    if Dict[key]['population'] > 1000000000:
        new_list += [key]
print(new_list)

# Sual 2
name = input("Please enter username: ")
password = input("Please enter password: ")
users = {
    "maximus":"password1",
    "asterix":"password2",
    "starrex":"password3"
}
if name in users:
    if users[name] == password:
        print(f"'{name}' salam, sisteme xos gelmisiniz!")
    else:
        print("Sifre duzgun deyil.")
else:
    print("Bele bir istifadeci yoxdur!")
"""
# Sual 3

