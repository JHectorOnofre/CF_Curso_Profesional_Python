#obtener máximo y mínimo dentro de una lista
# para cualquiera de los casos se requiere un punto de comparaciónpara saber si es
# un número mayor o menor que la referencia

lista = [2, 4, 5, 6, 1, 10, 9]

max = 0
for numero in lista:
    # "si max (0) es menor al número que estoy recorriendo, entonces el actual >max"
    if max < numero:
        max = numero #el nuevo max es asignado a la variable max
print(max) #10

print(min(lista))


## Caso para números negativos:
lista_negtiva = [-12, -4, -5, -6, -9, -19, -9]

max_negativo = lista_negtiva[0] #igualar al primer valor dentro de la lista

for numero in lista_negtiva:
    if max_negativo < numero:
        max_negativo = numero
print(max_negativo) #valor más grande en negativos es -4 (más pŕoximo a 0)


min_negativo = lista_negtiva[0]

for numero in lista_negtiva:
    if min_negativo > numero:
        min_negativo = numero
print(min_negativo)

