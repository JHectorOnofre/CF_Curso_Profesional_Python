
matriz = [
    [1, 3, 5, 6, 9], 
    [3, 2, 4, 5, 8], 
    [7, 1, 5, 0, 6] 
] 

## Con for: el primero recorre filas, el segundo columnas

print("recorrido mediante for: ")
for fila in matriz:
    for elemento in fila:
        print(elemento, end=" ") #imprime elementos espaciados
    print() #salto de linea al final de cada fila recorrida
    

## Recorrer con len(): saber la posición exacta
print("recorrido mediante for in range: ")
for fila2 in range(0, len(matriz)): #0 al total de filas 
    for elemento2 in range(0, len(matriz[fila2])):
        print(matriz[fila2][elemento2], end=" ")
    print()
        
