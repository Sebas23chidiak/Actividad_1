# Este código es general y permite a un usuario ingresar cualquier valor para X e Y y luego realiza una serie de operaciones con estos valores.
SUMA = 0  # Primero, inicializamos una variable llamada SUMA en 0.
X = float(input("Ingrese el valor de X: "))  # Solicitamos al usuario que ingrese el valor de X como un número decimal.
# En la siguiente línea de código, se suma el valor ingresado de X al valor actual de la variable SUMA y se actualiza SUMA con el nuevo resultado.
SUMA = SUMA + X
Y = float(input("Ingrese el valor de Y: "))  # Solicitamos al usuario que ingrese el valor de Y como un número decimal.
# A continuación, se realiza una operación en X donde se suma el cuadrado de Y al valor actual de X y se actualiza X con el nuevo resultado.
X = X + Y ** 2
# Luego, SUMA se actualiza nuevamente al sumar el resultado de la división de X entre Y al valor actual de SUMA.
SUMA = SUMA + X / Y
# Finalmente, se muestra en pantalla el valor final de la variable SUMA.
print("EL VALOR DE LA SUMA ES:", SUMA)
