import matplotlib.pyplot as plt
horas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
temperaturas = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 34, 33, 32, 31, 30,
29, 28, 27]
plt.fill_between(horas, temperaturas, color='skyblue', alpha=0.5)
plt.xlabel('Hora')
plt.ylabel('Temperatura (°C)')
plt.title("Evolucion de la temperatura a lo largo del día")
plt.show()