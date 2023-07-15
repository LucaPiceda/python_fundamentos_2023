capitalInicial = float(input("Ingrese su capital incial"))
anos=int(input("Ingrese la cantidad de años por las que quiere invertir su capital"))
interesPF=round(capitalInicial*(1+0.5)**anos,2)
#elevo al doble de la cantidad de años ya que el interés es semestral#
interesBonos=round(capitalInicial*(1+0.25)**(anos*2),2)
print("Resultado después de", anos, "años en Plazo Fijo: ", interesPF)
print("Resultado después de", anos, "años invirtiendo en Bonos: ", interesBonos)
if interesPF>interesBonos:
 print("Le conviene invertir en Plazo Fijo")

elif interesPF<interesBonos:
 print("Le conviene invertir en Bonos")
else:
 print("Ambas opciones le generan el mismo rendimiento")