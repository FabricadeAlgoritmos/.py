def fatorial(x):
    if x == 1 or x == 0 :
        return 1
    #fim if
    return x * fatorial(x - 1)
#fim da função

i = 0
while i <= 5 :
    print("%d! = %d" % ( (i), (fatorial(i)) ) )
    i = i + 1
#fim while
