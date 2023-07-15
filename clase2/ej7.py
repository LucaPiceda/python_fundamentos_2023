comenzar = input("Comenzamos?").lower()
continuar=comenzar
while (continuar == "si"):
 n = int(input("Ingrese un número"))
 sumaHastaN = (n*(n+1))//2
 print("la suma de los primeros ", n, "números enteros es ",sumaHastaN)
 continuar = input("¿Desea empezar devuelta?").lower()
print("Ok. Muchas gracias!")