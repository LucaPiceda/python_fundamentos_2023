def totalFactura(bruto, ivaPorc):
 iva = bruto * (ivaPorc / 100)
 total = bruto + iva
 return total
