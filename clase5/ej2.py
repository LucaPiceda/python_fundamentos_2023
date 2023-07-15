import matplotlib.pyplot as plt
meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']
lluvias = [100, 80, 120, 90, 70, 110, 130, 150, 140, 120, 100, 80]
plt.bar(meses, lluvias, color='red')
plt.xlabel('Meses')
plt.ylabel('Lluvias (mm)')
plt.title('Evolución de lluvias mensuales')
plt.show()