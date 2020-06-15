class Persona:
    def __init__(this,nombre,edad,*n,**d):
        this.nombre=nombre
        this.edad=edad
        this.tupla=n
        this.diccionario=d
    def desplegar(this):
        print("nombre: ",this.nombre)
        print("edad: ",this.edad)
        print("valores (tupla): ",this.tupla)
        print("diccionario: ",this.diccionario)
        
p1=Persona("juan",20)
p1.desplegar()
print()

p2=Persona("karla",30, 2,4,5)
p2.desplegar()
print()

p3=Persona("paola",33, 4,9, m="manzana",p="pera",j="jicama")
p3.desplegar()