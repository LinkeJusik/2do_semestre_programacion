class Rectangulo:
    def __init__(self, L1=10,L2=5):
        self.Lado1 = L1
        self.Lado2 = L2
    def CalcularArea(self):
        return self.Lado1 * self.Lado2
    def CalcularPerimetro(self):
        return 2 * (self.Lado1) + 2 * (self.Lado2)
    def ImprimirRectangulo(self):
        print("El área: ",self.CalcularArea())
        print("El perimetro: ",self.CalcularPerimetro())
        
obj = Rectangulo()
obj.ImprimirRectangulo()

obj2 = Rectangulo(20,30)
obj2.ImprimirRectangulo()
