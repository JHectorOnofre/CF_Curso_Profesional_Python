lista = ["g", "f", "e", "d", "c", "b", "a"]


### Imprimir al revés #1: for in
'''
indice = 6
nueva_lista = [lista[6]] = "a"
-1: indice = 5
nueva_lista = ["a", lista[5]] = ["a", "b"]
'''

nueva_lista_for = []

for indice in range(len(lista)-1, -1, -1):
    nueva_lista_for.append(lista[indice])

print(nueva_lista_for)


### método 2: función reversed()
nueva_lista_reversed = []

for letra in reversed(lista):
    nueva_lista_reversed.append(letra)

print(nueva_lista_reversed)


### método 3: función reverse (cambiar la lista original)
lista.reverse()
print(lista)
