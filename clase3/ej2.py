from datetime import date
anioHoy = int(date.today().year)
nacUsuario=int(input("Ingrese su año de nacimiento"))
while nacUsuario>anioHoy:
 print("Error, ingrese bien su año de nacimiento")
 nacUsuario=int(input())
edad = (anioHoy-nacUsuario)
mayorEdad = edad>=18
if mayorEdad:
 print("Usted es mayor de edad. Tiene ", edad, "años")
else:
 print("Usted no es mayor de edad. Tiene ", edad, "años")