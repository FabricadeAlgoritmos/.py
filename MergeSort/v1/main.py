vet1 = [2, 4, 6, 8, 10]
vet2 = [1, 3, 5, 7, 9]
vet3 = [None]*10;

i = 0
j = 0
k = 0

while(i < len(vet1) and j < len(vet2)):
    if(vet1[i] < vet2[j]):
        vet3[k] = vet1[i]
        i = i + 1
    else:
        vet3[k] = vet2[j]
        j = j + 1
    #fim if else
    k = k + 1
#fim while

while(i < len(vet1)):
    vet3[k] = vet1[i]
    i = i + 1
    k = k + 1
#fim while

while(j < len(vet1)):
    vet3[k] = vet2[j]
    j = j + 1
    k = k + 1
#fim while

print(vet3)
