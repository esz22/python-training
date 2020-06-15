class Rectangulo:
    
    def __init__(self, base, altura):
        self.base=base
        self.altura=altura
    def calcular_area(self):
        return self.base*self.altura

base=int(input("digite el valor de la base: "))
altura=int(input("digite el valor de la altura: "))
rectangulo1=Rectangulo(base,altura)
print("el area del rectangulo1 es: ",rectangulo1.calcular_area())


rectangulo2=Rectangulo(4,2)
print("el area del rectangulo2 es: ",rectangulo2.calcular_area())
