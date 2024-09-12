
## convertir tupla en una lista:
tupla_original = ("Python", "Java", "C#", "JavaScript", "Dart", "Swift")
print(f"La tupla es: {tupla_original}")

nueva_lista = list(tupla_original)
print(f"Ahora es una lista: {nueva_lista}")

print()
## convertir lista en tupla
lista_original = ["Django", "Spring", "Next.js", "Flutter"]
print(f"La lista es: {lista_original}")

nueva_tupla = tuple(lista_original)
print(f"Ahora es una tupla: {nueva_tupla}")


## Recorrer una tupla
print()
print("Recorriendo elementos de la tupla original:")
for elemento in tupla_original:
    print(elemento)