#imprimir solo las letras a contenidas en una cadena
for letra in "Holanda":
    if letra=="a":
        print(letra)
        break
else:
    print("fin del ciclo for")

print("continua el programa")


#imprimir solo numeros pares
for i in range(6):
    if(i%2==0):
        print(i)

for i in range(6):
    if(i%2!=0):
        continue
    print(i)


    