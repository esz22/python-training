class Caja:
    def __init__(self,largo,alto,ancho):
        self.largo=largo
        self.alto=alto
        self.ancho=ancho
    def volumen(self):
        return self.largo*self.alto*self.ancho

caja1=Caja(4,4,4)
print("el volumen de la caja1 es: ", caja1.volumen())