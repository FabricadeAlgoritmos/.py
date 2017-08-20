vetor = [0]*6
fim = 0;
vetor[fim] = int(input("Informe o valor ~:> "))
fim = fim + 1;
while fim < 6:
    aux = int(input("Informe o valor ~:> "))
    i = fim
    while i > 0 and aux < vetor[i - 1]:
        vetor[i] = vetor[i - 1]
        i = i - 1
    #fim while
    vetor[i] = aux
    fim = fim + 1
#fim while
print("\nMetodo de Ordenação: InsertionSort\n")
print(vetor)
