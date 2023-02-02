#Recursividad

#Función Factorial sin recursividad
def factorial(n):
    if n==0:
        return print(1)
    for x in range (1,n):
        n=n*x
    return print(n)

factorial(15)

#Funcion Factorial con recursividad
def factorial_r(n):
    if (n==0) or (n==1):
        return 1
    else:
        return n*factorial_r(n-1)

print(factorial_r(1))


#Fibonnaci sin recursividad
def fibonacci(n):
    f=[0,1]
    r=0
    for x in range (0,n-1):
        r=f[x]+f[x+1]
        f.append(r)
    return print(f[n])

fibonacci(1500)

#Fibonacci con Recursividad
def fibonacci_r(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci_r(n-1)+fibonacci_r(n-2)

print(fibonacci_r(1500))