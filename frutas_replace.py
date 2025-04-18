# Lista original con errores de escritura
frutas = ["mansana", "pela", "pina", "nalanja"]

# Nueva lista vacía para almacenar los nombres corregidos
frutas_correctas = []

# Recorremos cada fruta y corregimos con .replace()
for fruta in frutas:
    fruta = fruta.replace("mansana", "Manzana")
    fruta = fruta.replace("pela", "Pera")
    fruta = fruta.replace("pina", "Piña")
    fruta = fruta.replace("nalanja", "Naranja")
    frutas_correctas.append(fruta)

# Imprimir resultado final
print("frutas_correctas:")
print(frutas_correctas)
