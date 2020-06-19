nombres=["juan", "carla", "ricardo", "maria"]
print (nombres)
#conocer el largo de la lista
print(len(nombres))
#elementos de la lista
print(nombres[0])
print(nombres[1])
print(nombres[2])
print(nombres[3])
#navegacion inversa de la lista
print(nombres[-1])
print(nombres[-2])
print(nombres[-3])
print(nombres[-4])
#imorimir el rango de la lista
print(nombres[0:2])#sin incluir el indice 2
#imprimir el rango de la lista sin incluir el indice 3
print(nombres[0:3])
#imprimir los elementos hasta el final desde el indice proporcionado
print(nombres[1:])
#cambiar los elementos de una lista
nombres[3]="ivone"
print(nombres)
#iterar la lista
for nombre in nombres:
    print(nombre)
#revisar si existe un elemento dentro de la lista
if("carla") in nombres:
    print("carla si existe en la lista")
else:
    print("carla no existe en la lista")
#agregar un nuevo elemento a la lista
nombres.append("enrique")
print(nombres)
#agregar un elemento en una parte especifica de la lista
nombres.insert(1,"octavio")
print(nombres)
#remover un elemento de la lista 
nombres.remove("octavio")
print(nombres)
#remover el ultimo elemento de la lista
nombres.pop()
print(nombres)
#remover el indice indicado en la lista
del nombres[0]
print(nombres)
#limpiar todos los elementos de la lista
nombres.clear()
print(nombres)
#eliminar por completo la lista
del nombres
print(nombres)
