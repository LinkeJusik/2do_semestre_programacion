def Fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    elif n>1:
        return Fibonacci(n-1) + Fibonacci(n-2)
    else:
        return "Necesito un número entero positivo, por el amor de dios"
    
a=int(input("Introduce el n'simo número de Fibonacci que deseas calcular: "))
print("El elemento número",a,"de Fibonacci es:",Fibonacci(a))