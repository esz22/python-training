#a=3
a=int(input("proporciona un valor: "))
valormin=0
valormax=5
dentroRango=(a>=valormin and a<=valormax)
if(dentroRango):
    print("dentro de rango")
else:
    print("fuera de rango")


vacaciones=True
diaDescanso=False
if(vacaciones or diaDescanso):
    print("Puedes ir al parque")
else:
    print("Tienes deberes que hacer")
    

print(not(vacaciones))