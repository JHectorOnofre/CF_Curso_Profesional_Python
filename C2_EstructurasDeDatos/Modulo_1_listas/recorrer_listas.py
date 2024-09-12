lista = ["a", "b", "c", "d", "e"]

#for variable recorrer (in) la estructura (lista)
for letra in lista:
    print(letra) 
    #imprime los elementos recorridos de la lista guardados en la variable letra

'''
range (inicio, fin, paso)
indice = 0
print(lista[0])
indice = 1
print(lita[1])
... hasta completar el tamaño total de la lista dada por la función (len)
'''
for indice in range(0, len(lista)): 
    print(lista[indice]) 

