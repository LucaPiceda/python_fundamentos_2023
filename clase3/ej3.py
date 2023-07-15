password = input("Ingrese la contraseña")
contador = 0
while (contador<4 and password !="123456"):
 contador+=1
 print("Contraseña incorrecta, intente nuevamente, le quedan",
 5 - contador,"intentos")
 password=input()

if password=="123456":
 print("Bienvenido")
else:
 print("acceso bloqueado")