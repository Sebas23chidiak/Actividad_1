# Ingreso de datos: Comenzamos pidiendo la edad de Juan para calcular las edades de Ana y Alberto, y luego sumamos estas tres edades para obtener la edad de la mamá.
juan = int(input("Ingrese la edad de Juan: "))  # Solicitamos la edad de Juan como un número entero.
# Proceso: Calculamos las edades de los dos hermanos y la mamá.
alberto = int((2/3) * juan)  # Calculamos la edad de Alberto, que es el 2/3 de la edad de Juan.
ana = int((4/3) * juan)  # Calculamos la edad de Ana, que es el 4/3 de la edad de Juan.
mama = int(juan + alberto + ana)  # Sumamos las edades de los tres hermanos para obtener la edad de la mamá.
# Resultados: Utilizamos print para mostrar las edades de Juan, sus hermanos y la mamá.
print("La edad de Juan es:", juan) # Nos mostrara la edad de Juan.
print("La edad de Alberto es:", alberto) # Nos mostrara la edad de Alberto.
print("La edad de Ana es:", ana) # Nos mostrara la edad de Ana.
print("La edad de la mamá es:", mama) # Nos mostrara la edad de la Mamá.
