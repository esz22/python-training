#set es una coleccion sin orden y tampoco tienen indices, 
# no permite elementos repetidos y los elementos no se pueden modificar 
# pero si agregar nuemos o eliminar

planetas={"marte", "jupiter", "venus"}
print(planetas)
#largo
print(len(planetas))
#revisar si un elemento esta presente
print("marte" in planetas)
#agregar
planetas.add("tierra")
print(planetas)
planetas.add("tierra")#no permite elementos duplicados
print(planetas)
#eliminar con remove posiblenete arroja excepcion
planetas.remove("tierra")
print(planetas)
#eliminar con discard no arroja excepcion
planetas.discard("jupiter")
print(planetas)
#limpiar el set
planetas.clear()
print(planetas)
#eliminar el set
del planetas
print(planetas)