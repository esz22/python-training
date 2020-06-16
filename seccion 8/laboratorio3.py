class Persona:
    def __init__(self,nombre,edad,*n,**d):
        self.nombre=nombre
        self.edad=edad
        self.tupla=n
        self.diccionario=d
    def desplegar(self):
        print("nombre: ",self.nombre)
        print("edad: ",self.edad)
        print("valores (tupla): ",self.tupla)
        print("diccionario: ",self.diccionario)
        
p1=Persona("juan",20)
p1.desplegar()
print()

p2=Persona("karla",30, 2,4,5)
p2.desplegar()
print()

p3=Persona("paola",33, 4,9, m="manzana",p="pera",j="jicama")
p3.desplegar()