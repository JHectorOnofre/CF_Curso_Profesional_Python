### Sets (conjutos): Para almacenar distintos elementos
'''
* los elementos que se guardan no tienen un orden, no se pueden 
consultar sus elementos con base a su índice
* los elementos repetidos dentro de un set no se imprimen
* los elementos no se imprimen en orden
* son una estructura inmutable
'''

# 2 sintaxis
set1 = {1, 2, 3, 4, 4, 4}
set2 = set([1, 2, 3, 4, 4, 6])

print(set1) #no imprime números "4" repetidos


#recorrer un Set
for elemento in set1:
    print(elemento)
    
    
#saber si existe un elemento dentro de un set
print(4 in set1) #true, el número 4 si está
print("4" in set1) #false, se busca una cadena
