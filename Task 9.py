"""# Sual 1
import random
N = int(input("N-i daxil edin: "))
M = int(input("M-i daxil edin: "))
matrix = [[random.randint(-10,10) for _ in range(N)] for _ in range(M)]
for row in matrix:   # Matrixi daha sade gostermek ucun
    print(row)
# a), b) 
mutleq_cem = 0
kvadrat_cem = 0
for row in matrix:
    for i in row:
        mutleq_cem += abs(i)
        kvadrat_cem += i*i
print("Mutleq qiymetler cemi:",mutleq_cem)
print("Kvadratlar cemi:", kvadrat_cem)
# c)
K = int(input("K-setrin daxil et: ")) - 1
hasil = 1
for i in matrix[K]:
    hasil*=i
print(hasil)
# d)
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
"""
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
k = int(input("k-ni daxil edin: "))
m = int(input("m-i daxil edin: "))
massiv_B = []
row_k = matrix_A[k]
col_m = [row[m] for row in matrix_A]
for i in range(n):
    massiv_B += [row_k[i] * col_m[i]]
print("B massivi=", massiv_B)
# c)
diaqonal_A = []
for i in range(n):
    for j in range(n):
        if i == j:
            diaqonal_A += [matrix_A[i][j]]
for i in range(n):
    massiv_B += [row_k[i] / diaqonal_A[i] if diaqonal_A[i] != 0 else "-"]
print(massiv_B)
# d)
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
    



