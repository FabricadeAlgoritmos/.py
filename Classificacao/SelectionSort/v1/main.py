vet = [5, 4, 3, 2, 1]
i = 0
while i < len(vet) - 1:
    menor = i
    j = menor + 1
    while j < len(vet):
        if vet[menor] > vet[j]:
            menor = j
        #fim if
        j = j + 1
    #fim while
    aux = vet[i]
    vet[i] = vet[menor]
    vet[menor] = aux
    i = i + 1
#fim while

print(vet)
