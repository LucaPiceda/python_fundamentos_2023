cantPersonas = int(input("ingrese la cantidad de personas que van a comer"))
dineroComensal =float(input("Ingrese cuanto dinero lleva c/u"))
precioPlato = float(input("Ingrese el precio de cada plato"))
dineroTotal = cantPersonas*dineroComensal
platosAComer = round(dineroTotal/precioPlato)
print("Comerán", platosAComer, "platos")