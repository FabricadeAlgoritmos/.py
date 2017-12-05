vetor = [5, 4, 3, 2, 1]
max = 4
troca = 1

while troca != 0 :
    troca = 0
    i = 0
    while i <= max - 1 :
        if vetor[i] > vetor[i + 1]:
            aux = vetor[i]
            vetor[i] = vetor[i + 1]
            vetor[i + 1] = aux
            troca = 1
        #fim if
        i = i + 1
    #fim while
    max = max - 1
#fim while

print(vetor) 