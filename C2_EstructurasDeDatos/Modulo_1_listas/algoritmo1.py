#obtener la sumatoria de una lista

lista = [2, 4, 5, 6, 1, 10, 9]

#1 se crea una variable en la cual se guarde el recorrido 
sumatoria = 0

#2 se hace el recorrido mediante un ciclo for

for numero in lista:
    sumatoria += numero #agrega a la variable los valores recorridos
    
print(f"Resultado sumatoria = {sumatoria}")

#3 se calcula el promedio de la lista:
promedio = 0

for num in lista:
    #suma todos los numeros, luego divide / numero elementos:
    promedio += num 

promedio /= len(lista)
print(promedio)
