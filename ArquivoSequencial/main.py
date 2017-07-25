
# declarando as listas
listaVelha = [1, 5, 25,65, 98, 101, 220]
lote = [2, 60, 79, 80]

print ("Lista velha: ", listaVelha, len(listaVelha), "elementos")
print ("Lote", lote, len(lote), "elementos\n")

size = (len(listaVelha) + len(lote))
novaLista = [0]*size 
#print(novaLista, "tem", len(novaLista), "elementos")

print("\nInserindo dados...")

i = 0
j = 0 
k = 0

while i < len(listaVelha) and j < len(lote):
    if listaVelha[i] < lote[j]:
        novaLista[k] = listaVelha[i]
        i = i + 1
    else:
        novaLista[k] = lote[j]
        j = j + 1
    #fim else
    k = k + 1
#fim while
while i < len(listaVelha):
    novaLista[k] = listaVelha[i]
    i = i + 1 
    k = k + 1
#fim while

while j < len(lote):
    novaLista[k] = lote[j]
    j = j + 1
    k = k + 1
#fim while

print ("Nova lista: ", novaLista, len(novaLista), "elementos")

print ("\nBuscando dados...")
cod = int(input("Informe a chave de busca ~:> "))
inicio = 0
final = (len(novaLista) - 1)
meio = int((inicio + final) / 2)
while cod != novaLista[meio] and inicio < final:
    if cod > novaLista[meio]:
        inicio = meio + 1
    else:
        final = meio - 1
    #fim else
    meio = int((inicio + final) / 2)
#fim while
if cod == novaLista[meio]:
    print(novaLista[meio], "encontrado na posicao", meio, "!")
#fim if

print ("\nRemovendo dados...")
novoLote = [5, 25, 79, 220]
size = (len(novaLista) - len(novoLote))
listaAtualizada = [0]*size

i = 0
j = 0
k = 0

while j < len(novoLote):
    if(novaLista[i] != novoLote[j]):
        listaAtualizada[k] = novaLista[i]
        print("Lista[{}] recebe {}".format(k, novaLista[i]))
        k = k + 1
    else:
        print(novoLote[j], "removido!")
        j = j + 1
    #fim else
    i = i + 1
#fim while

while i < len(novaLista):
     listaAtualizada[k] = novaLista[i]
     print("Lista{} recebe {}".format(k, novaLista[i]))
     k = k + 1
     i = i + 1
#fim while

print("Lista Atualizada: ", listaAtualizada, len(listaAtualizada), "elementos")