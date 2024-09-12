#generador que permita itearar números pares de 0 a 100

def pares(): #Generador -> Lazy iterator
    for numero in range(0,100,2):
        yield numero #retornar valores sin finalizar la funcion
        
        print("se reaunda la ejecución")

for par in pares():
    print(par)