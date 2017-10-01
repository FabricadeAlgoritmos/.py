vet = [32, 18, 45, 29, 16, 41, 30, 27 , 14, 37, 29, 38, 20, 32, 17, 26]

inc = [8, 4, 2, 1]

x = 0

while inc[x] > 1 :
    i = 0
    j = inc[x]
    while j < len(vet):
        if vet[i] > vet[j]:
            aux = vet[i]
            vet[i] = vet[j]
            vet[j] = aux
        #fim if
        i = i + 1
        j = j + 1
    #fim while
    x = x + 1
#fim while

def insertion(v):
    i = 1
    while i < len(v):
        j = i
        while v[j] < v[j - 1] and j > 0 :
            aux = v[j]
            v[j] = v[j - 1]
            v[j - 1] = aux
            j = j - 1
        #fim while
        i = i + 1
    #fim while
    #print(v)
    #return v
#fim da funcão

insertion(vet)
print(vet)
