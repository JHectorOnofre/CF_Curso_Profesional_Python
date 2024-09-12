### funciones len(), max(), min(), sum(), sorted()
# Funciones aplicables para estructuras de datos iterables

tupla = (1, 2, 3, 4, 5, 6, 7)
tupla_2 = (1, 2, 4, 6, 9, 10)

#len() verificar el tamaño total de elementos de una tupla
print(len(tupla))

#max() el valor máximo en la tupla
print(max(tupla))

#min() el valor mínimo en la tupla
print(min(tupla))

#sum() sumatoria de todos los elemenots
print(sum(tupla))


#sorted() ordenar una tupla, permite 3 parámetros:
'''
(estrucutra a ordenar, 
una llave o función para hacer el ordenamiento, 
permite enviar un reverse por medio de True o False)
 '''
print(sorted(tupla)) #devuelve como resultado una lista

print(sorted(tupla, reverse=True)) #orden descendiente
