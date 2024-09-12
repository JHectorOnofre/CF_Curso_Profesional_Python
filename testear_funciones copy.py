# DocSring
# __doc__

def suma(numero_1, numero_2):
    """ #1 se describe el comportamiento de la función:
    la función suma 2 números enteros:
    argumentos: numero_1 (int), numero_2 (int)
    se retorna: la suma de los parámetros
    
    #2 colocar las pruebas del correcto funcionamiento, 
    simulando su comportamiento en consola:
    
    >>> suma(15, 40)
    55
    
    >>> suma(15, 15)
    30
    """
    return numero_1 + numero_2


def resta(numero_1, numero2):
    """
    >>> resta(100, 200)
    -100
    """
    return numero_1 - numero2
    #desde consola: $python3 -m doctest testear_funciones.py

#El DocString se almacena en el atributo __doc__ de la función

#print(suma.__doc__)
#print(help(suma))
