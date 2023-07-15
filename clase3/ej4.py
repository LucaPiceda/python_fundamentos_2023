harina= float(input("Ingrese los kilos de harina"))
azucar= float(input("Ingrese los kilos de azucar"))
manteca= float(input("Ingrese los kilos de manteca"))
posibilidad = harina>=5 and azucar >=1 and manteca>=2
if posibilidad:
 print("Puede realizar la receta")
else:
 print("No puede preparar la receta")