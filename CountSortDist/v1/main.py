vet = [26, 19, 34, 19, 23, 16, 31, 26, 31, 22, 21, 29];

def getMax(vet):
    m = vet[0]
    i = 1
    while i < len(vet):
        if vet[i] > m :
            m = vet[i]
        #fim if
        i = i + 1
    #fim while
    return m
#fim getMax

def getMin(vet):
    m = vet[0]
    i = 1
    while i < len(vet):
        if vet[i] < m :
            m = vet[i]
        #fim if
        i = i + 1
    #fim while
    return m
#fim getMin

maior = getMax(vet)
menor = getMin(vet)
#print("Maior: ", maior, "\nMenor: ", menor)

cont = [0]*(maior + 1)

i = 0
while i < len(vet):
    cont[vet[i]] = cont[vet[i]] + 1
    i = i + 1
#fim while

i = menor + 1
while i <= maior:
    cont[i] = cont[i] + cont[i - 1]
    i = i + 1
#fim while

j = 0
saida = [None]*len(vet)
while j < len(vet):
    i = cont[vet[j]]
    saida[i - 1] = vet[j]
    cont[vet[j]] = cont[vet[j]] - 1
    j = j + 1
#fim while
print(saida)
