class Persona:
       
    def __init__(self, nombre, edad):
        self.nombre=nombre
        self.edad=edad

Persona.nombre="juan"
Persona.edad=28

print(Persona.nombre)
print(Persona.edad)


# creacion de un objeto
persona1=Persona("enrique",22)

print(persona1.nombre)
print(persona1.edad)
print(id(persona1))

#creacion de otro objeto
persona2=Persona("juan",20)
print(persona2.nombre)
print(persona2.edad)
print(id(persona2))

