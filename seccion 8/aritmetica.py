class Aritmetica:
    
    def __init__(self,operando1,operando2):
        self.operando1=operando1
        self.operando2=operando2
    
    def sumar(self):
        """comentario parte de la clase"""
        return self.operando1+self.operando2
    
#Crear un objeto
ar1=Aritmetica(2,4)
print("Resultado de la suma: ",ar1.sumar())

