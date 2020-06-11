#un diccionario esta compuesto de llave,valor (key, value)
diccionario={
    "IDE":"integrated development environment",
    "OOP":"objet oriented programming",
    "DBMS":"database management system"
}
print(diccionario)
#largo
print(len(diccionario))
#accediendo a un elemento
print(diccionario["IDE"])
#otra forma de acceder
print(diccionario.get("OOP"))
#modificando valores
diccionario["IDE"]="INTEGRATED DEVELOPMENT ENVIRONMENT"
print(diccionario)
#iterar elementos
for termino in diccionario:
    print(termino)
for termino in diccionario:
    print(diccionario[termino])
for valor in diccionario.values():
    print(valor)
#comprovar si un elemento existe
print("IDE"in diccionario)
#agregar nuevos elementos
diccionario["PK"]="primary key"
print(diccionario)
#remover elementos
diccionario.pop("DBMS")
print(diccionario)
#limpiar diccionario
diccionario.clear()
print(diccionario)
#eliminar por completo
del diccionario
print(diccionario)