condicion=True
if(condicion==True):
    print("la condicion es verdadera")
elif(condicion==False):
    print("la condicion es falsa")
else:
    print("condicion no reconocida")


print("condicion verdadera") if condicion else print("condicion falsa")

numero=int(input("proporciona un numero entre 1 y 3: "))

if(numero==1):
    numeroTexto="numero uno"
elif(numero==2):
    numeroTexto="numero dos"
elif(numero==3):
    numeroTexto="numero tres"
else:
    numeroTexto="valor fuera de rango"
print("numero proporcionado: ",numeroTexto)


