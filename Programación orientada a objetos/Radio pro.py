class RadioMP3():
    def __init__(self, Frec=99.9,Vol=45):
        self.Frecuencia = Frec
        self.Volumen = Vol
    def AumentarFrec(self):
        if(obj.Frecuencia==115.3):
            print("La frecuencia no puede aumentar más de 115.3")
        else:
            self.Frecuencia += 0.1
    def DisminuirFrec(self):
        if(obj.Frecuencia==60.1):
            print("La frecuencia no puede bajar de los 60.1")
        else:
            self.Frecuencia -= 0.1
    def SubirVol(self):
        if(obj.Volumen==60):
            print("El volumen no puede aumentar más de 60")
        else:
            self.Volumen += 1
    def BajarVol(self):
        if(obj.Volumen==0):
            print("El volumen no puede ser menor de 0")
        else:
            self.Volumen -= 1
    def Imprimir(self):
        print("El volumen es de", self.Volumen)
        print("La frecuencia es de", self.Frecuencia)

obj = RadioMP3()
while True:
    while True:
        try:
            a=int(input("Elige que deseas hacer:\n1. Aumentar la frecuencia\n2. Disminuir la frecuencia\n3. Aumentar el volumen\n4. Disminuir el volumen\n5. Imprimir los datos\n6. Imprimir los datos y salir\n"))
            break
        except:
            print("Dato no valido")
            
    if(a==1):
        obj.AumentarFrec()
    elif(a==2):
        obj.DisminuirFrec()
    elif(a==3):
        obj.SubirVol()
    elif(a==4):
        obj.BajarVol()
    elif(a==5):
        obj.Imprimir()
    elif(a==6):
        obj.Imprimir()
        break