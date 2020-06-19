#tupla mantiene el orden pero ya no se puede modificar
frutas=("naranja","platano","guayaba")
print(frutas)
#saber el largo de la tupla
print(len(frutas))
#accediendo a un elemento
print(frutas[0])
#navegacion inversa
print(frutas[-1])
#rango
print(frutas[0:2])#excluyendo el indice 2
#modificar un valor
#frutas[0]="naranjita"
#convertir tupla a lista
frutaLista=list(frutas)
frutaLista[1]="platanito"
frutas=tuple(frutaLista)
print(frutas)
del frutaLista
#iterar una tupla
for fruta in frutas:
    print(fruta,end=", ")
#no podemos agregar ni eliminar elementos de una tupla
del frutas
print(frutas)


