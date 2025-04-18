# Lista con frases mal escritas
frases = [
    "Vivo en Madrid, la capital de Espana.",
    "El pais más grande es Russia.",
    "Paris es una ciudad muy romantica.",
    "La ciudad de Norkolk es conocida por su puerto."
]

# Lista vacía para las frases corregidas
frases_corregidas = []

# Corrección de cada frase
for frase in frases:
    frase = frase.replace("Espana", "España")
    frase = frase.replace("pais", "país")
    frase = frase.replace("Paris", "París")
    frase = frase.replace("Norkolk", "Norfolk")
    frases_corregidas.append(frase)

# Imprimir resultado final
print("frases_corregidas:")
print(frases_corregidas)
