print("proporcione los siguientes datps del libro: ")
nombre=input("proporciona el nombre: ")
ID=int(input("proporciona el ID: "))
precio=float(input("proporciona el precio: "))
envioGratuito=input("indica si el envio es gratuito (True/False): ")

if(envioGratuito=="True"):
    envioGratuito=True
elif(envioGratuito=="False"):
    envioGratuito=False
else:
    envioGratuito="Valor incorrecto, debe ser True/False"

print("Nombre: ",nombre)
print("ID: ", ID)
print("Precio: ", precio)
print("Envio gratuito: ", envioGratuito)

