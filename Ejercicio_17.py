# Importamos la biblioteca math para utilizar la constante math.pi, que representa el número pi.
import math
radio_circulo = float(input("Ingrese el radio del círculo: ")) # Solicitamos al usuario ingresar el radio de un círculo.
area_circulo = math.pi * (radio_circulo ** 2) # Calculamos el área del círculo utilizando la fórmula A = π * r^2.
circunferencia_circulo = 2 * math.pi * radio_circulo # Calculamos la longitud de la circunferencia utilizando la fórmula C = 2πr.
# Mostramos los resultados del área y la circunferencia.
print("El área del círculo es:", area_circulo)
print("La longitud de la circunferencia es:", circunferencia_circulo)
