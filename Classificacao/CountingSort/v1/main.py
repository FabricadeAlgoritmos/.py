vet = [5, 4, 3, 2, 1]
count = [0]*5
saida = [None]*5
i = 0

while i < len(vet) - 1 :
    j = i + 1
    while j < len(vet) :
        if vet[i] > vet[j]:
            count[i] = count[i] + 1
        else:
            count[j] = count[j] + 1
        #fim else
        j = j + 1
    #fim while j
    i = i + 1
#fim while i

i = 0
while i < len(vet):
    saida[count[i]] = vet[i]
    i = i + 1
#fim while

print(saida)
