def fibonacci(x):
    if x == 0 or x == 1:
        return 1
    #fim if
    return fibonacci(x - 1) + fibonacci(x - 2)
#fim da função

i = 0
while i <= 10 :
    print("%d" % (fibonacci(i)))
    i = i + 1
#fim while
