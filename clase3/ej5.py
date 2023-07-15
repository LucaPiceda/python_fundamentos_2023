edad = int(input("Ingrese su edad"))
bebe = edad<=2
infante = edad<=4
nino = edad<=10
adolescente = edad<=18
adulto = edad<=65
if bebe:
 print("No paga ingreso")
elif infante:
 print("Paga 100 pesos")
elif nino:
 print("Paga 200 pesos")
elif adolescente:
 print("Paga 400 pesos")
elif adulto:
 print("Paga 1000 pesos")
else:
 print("Paga 500 pesos")