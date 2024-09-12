
def pares():
    for numero in range(0,10,2): 
        yield numero
        
        print("se reaunida la ejecución")

generador = pares() #se comienza el generador

'''
Se prueba que, mediante un ciclo while infinito se obtengan 
valores del generador mas allá de los definidos en la funcion
(0 a 10) cuando el generador quede sin valores por retornar
generamos un mensaje de aviso
'''
while True:
    try: 
        par = next(generador)
        print(par)
    except StopIteration:
        print("el generador ya ha finalizado")
        break #generador sin valores? rompemos el ciclo

