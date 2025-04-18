# Lista original con errores de escritura
comidas = ["hamburgesa", "pitsa", "papas fritass", "perrito calientee"]

# Lista vacía para las comidas corregidas
comidas_corregidas = []

# Corrección de cada comida usando .replace()
for comida in comidas:
    comida = comida.replace("hamburgesa", "hamburguesa")
    comida = comida.replace("pitsa", "pizza")
    comida = comida.replace("papas fritass", "papas fritas")
    comida = comida.replace("perrito calientee", "perrito caliente")
    comidas_corregidas.append(comida)

# Imprimir resultado final
print("comidas_corregidas:")
print(comidas_corregidas)
