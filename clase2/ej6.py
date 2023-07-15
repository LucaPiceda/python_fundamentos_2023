num1 = int(input("Ingrese el primer entero positivo: "))
while num1<=0:
 print("Positivo dijimos, intente nuevamente")
 num1 = int(input("Ingrese el primer entero positivo: "))

num2 = int(input("Ingrese el segundo entero positivo: "))
while num2<=0:
 print("Positivo dijimos, intente nuevamente")
 num2 = int(input("Ingrese el segundo entero positivo: "))
#Me aseguro que el numero 1 sea el mas pequeño
if num1>num2:
 num1,num2 = num2,num1
suma = 0
for num in range(num1, num2 + 1):
 suma += num
print ("la suma de los numeros enteros entre", num1,"y",num2, "es:", suma)