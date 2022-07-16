from numpy import *
from matplotlib import *
from math import *
import math as mt
import matplotlib.pyplot as plt

while True:
    while True:
        try:
            vi=float(input("Ingrese una velocidad inicial\n"))
            break
        except:
            print("Tiene que ser un número")
    
    b=arange(0,mt.pi/2,0.05)
    d=zeros(len(b))
    suma=0
    
    for i in range(0,len(b),1):
        suma=(vi/9.9) * mt.sin(2* b[i])
        d[i]=suma
        
    plt.plot(b,d)
        
    z=input("¿Deseas agregar otra velocidad inicial?\nEscribe 'no' para acabar o cualquier otra cosa para seguir\n")
    if z.lower()=="no":
        break

plt.show()
print("Recuerda que pi/4 es igual a",mt.pi/4,"\nO sea, que es el valor máximo mostrado en esta grafica")
print("\nGracias por participar")