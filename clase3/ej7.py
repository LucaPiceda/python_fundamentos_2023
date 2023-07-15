palabras = []
print("Ingrese una palabra cualquiera. Si quiere terminar ingrese salir:")
for palabra in range(1000):
 palabra = input()
 if palabra.lower() == 'salir':
    break
 palabras.append(palabra)
print(palabras)