# Sual 1
import random
N = int(input("N-i daxil edin: "))
M = int(input("M-i daxil edin: "))
matrix = [[random.randint(-10,10) for _ in range(N)] for _ in range(M)]
for row in matrix:
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
