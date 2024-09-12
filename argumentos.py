# Crear funciones que puedan recibir n cantidad de argumentos

#Ejemplo de función con un solo argumento:
def promedio(listado):
    return sum(listado) / len(listado)

resultado = promedio([10, 10, 5, 7, 9]) #lista
print(resultado)


'''
Ejemplo con múltiples argumentos, todos aquellos valores de
los cuales se quiere obtener el promedio
'''
def promedio_args(*args):
    print(args) #imprime los valores guardados en "resultado2"
    print(type(args)) #tipo 'tuple'
    
    return sum(args) / len(args)

resultado2 = promedio_args(9, 7 , 8, 10, 6) #Tupla
print(resultado2)


#Ejemplo 3: cominando parámetros y args
def combinación (p1, p2, *args, p4=600):
    print(p1)
    print(p2)
    print(args)
    print(p4)
    
combinación (10, 5, 7, 8, 7 , 4, 5, 9, p4=8750)
