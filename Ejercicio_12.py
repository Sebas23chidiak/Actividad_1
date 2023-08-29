# Este código es general va a permitir que al usuario ingresar cualquier cantidad de horas de trabajo, tarifa por hora y retención en la fuente.
# Solicitamos al usuario ingresar el número de horas trabajadas.
horas_tra = float(input("Ingrese el número de horas trabajadas: "))
# Solicitamos al usuario ingresar la tarifa por hora.
tar_hora = float(input("Ingrese la tarifa por hora: "))
# Solicitamos al usuario ingresar el porcentaje de retención.
por_retencion = float(input("Ingrese el porcentaje de retención (%): "))
sala_bruto = horas_tra * tar_hora # Calculamos el salario bruto multiplicando las horas trabajadas por la tarifa por hora.
retencion_fuente = (por_retencion / 100) * sala_bruto # Calculamos la retención en la fuente dividiendo el porcentaje de retención entre 100 y luego multiplicando por el salario bruto.
sala_neto = sala_bruto - retencion_fuente # Calculamos el salario neto restando la retención en la fuente al salario bruto.
# Imprimimos los resultados.
print("Salario bruto:", sala_bruto)
print("Retención en la fuente:", retencion_fuente)
print("Salario neto:", sala_neto)
