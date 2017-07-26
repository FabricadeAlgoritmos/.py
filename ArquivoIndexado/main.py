from Usuario import Usuario
from Indice import Indice

#Criando um vetor de Objetos
u = [None]*10
#inicializando lista de usuarios
u[0] = Usuario(10, "Jane", True)
u[1] = Usuario(2, "Zoe", True)
u[2] = Usuario(11, "Max", True)
u[3] = Usuario(9, "Dip", True)
u[4] = Usuario(20, "Meg", True)

final = 4

index = [None]*10
#inicializando arquivo de indice
index[0] = Indice(2, 1)
index[1] = Indice(9, 3)
index[2] = Indice(10, 0)
index[3] = Indice(11, 2)
index[4] = Indice(20, 4)

def showUser(vetor = []):
    print ("\nLista de Usuarios")
    for lista in vetor: # percorre todos os elementos do array
        if lista != None:
             print ("[id=>", lista.id, ",\tnome=>", lista.nome, ",\tstatus=>", lista.status,"]")
        else:
            break
        #end else
    # end for
#end função

showUser(u)

def showIndex(vetor = []):
    print("\nArquivo de Indice")
    for lista in vetor:
        if lista != None:
            print ("[cod=>", lista.cod, ",\tpos=>", lista.pos, "]")
        else:
            break
        #fim else
    #fim for
#fim função

showIndex(index)

print ("\nInserindo novo Usuario...")
if final < 10:
    final = final + 1
    u[final] = Usuario(0, "Lain", True)

    aux = final - 1
    while aux >= 0 and u[final].id < index[aux].cod:
        index[aux + 1] = Indice(index[aux].cod, index[aux].pos)
        aux = aux - 1
    #fim while
    index[aux + 1].cod = u[final].id
    index[aux + 1].pos = final
#fim if

showUser(u)
showIndex(index)

print ("\nBuscando um Usuario...")
codigo = int(input("Informe o codigo de busca ~:> "))
inicio = 0
fim = final
meio = int((inicio + fim) / 2)
while codigo != index[meio].cod and inicio < fim:
    if codigo > index[meio].cod:
        inicio = meio + 1
    else:
        fim = meio - 1
    #fim else
    meio = int((inicio + fim) / 2)
#fim while

i = index[meio].pos
if codigo == u[i].id and u[i].status == True:
    print(u[i].nome, "encontrado na posicao", meio, "do indice e, ", i, "da lista.")
else:
    print("Codigo não existe na lista!")
#fim else

print("\nRemovendo um Usuario...")
codigo = int(input("Informe o codigo de busca ~:> "))
inicio = 0
fim = final
meio = int((inicio + fim) / 2)
while codigo != index[meio].cod and inicio < fim:
    if codigo > index[meio].cod:
        inicio = meio + 1
    else:
        fim = meio - 1
    #fim else
    meio = int((inicio + fim) / 2)
#fim while

i = index[meio].pos
if codigo == u[i].id and u[i].status == True:
    u[i].status = False
    print(u[i].nome, "removido logicamente!")
else:
    print("Codigo não existe na lista!")
#fim else

print("\nImprimindo...")
i = 0
while i <= final:
    if u[i].status:
        print ("[id=>", u[i].id, ",\tnome=>", u[i].nome, ",\tstatus=>", u[i].status,"]")
    #fim if
    i = i + 1
#fim while

print("\nAtualizando listas...")
newList = [None]*10
i = 0
k = 0
while i <= final:
    j = index[i].pos
    if u[j].status:
        newList[k] = Usuario(u[j].id, u[j].nome, True)
        index[k].cod = newList[k].id
        index[k].pos = k
        k = k + 1
    #fim if
    i = i + 1
#fim while
index[k] = None
final = k - 1
print ("Listas atualizadas...")
showUser(newList)
showIndex(index)