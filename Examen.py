def Dec_Bin(n):
    n=int(n)
    if n>0:
        if n>1:
            a=Dec_Bin(n/2)
            b=n%2
            return (a*10)+b
        else:
            return 1
    elif n<0:
        n=n*(-1)
        n=Dec_Bin(n)
        return n*(-1)
    else:
        return 0

b=0
while b==0:
    while True:
        try:
            x=int(input("Ingresa el número que deseas comprobar si es malvado o no: "))
            break
        except:
            print("Ingresa un número natural, por favor")
    if x<=0:
        print("Necesito un número natural D:")
    else:
        b+=1

c=Dec_Bin(x)
cont=0

d=str(c)

cont=d.count("1")

if(cont%2==0):
    print("Tu número",x,"(que en binario es",c,") SÍ es un número malvado :o")
else:
    print("Tu número",x,"(que en binario es",c,") NO es un número malvado :(")