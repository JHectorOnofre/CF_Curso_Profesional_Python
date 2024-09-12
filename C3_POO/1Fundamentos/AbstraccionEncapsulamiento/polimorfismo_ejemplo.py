#Un método que indica cuál es el mayor y menor

'''
#Sin polimorfismo
def retornaElMayor(a,b):
    #permite saber si un objeto está instanciado (viene de otra clase)
    if isinstance(a, int) and isinstance(b, int):
        if a > b:
            return a
        return b
    if isinstance(a, str) and isinstance(b, str): #se debe ordenar alfabéticamente
         cadena = [a,b]
         cadena.sort()
         return cadena[0] #retorna el primero [0]que resulte mayor con sort()
    
    if isinstance(a, list) and isinstance(b, list):
        if len(a) > len(b):
            return a
        return b
    
print(retornaElMayor(10,2))
print(retornaElMayor("hola","holaa"))
print(retornaElMayor( [1,2,3], [1,2]))

    #Agregar commparaciones de otros tipos de datos conlleva agragar más codigo específico
'''

#Aplicando Polimorfismo
class Numero:
    value = 0
    
    def __init__(self, value):
        self.value = value
        
    def comparar(self, numero): #metodo que recibe otra instancie de la misma clase
        if numero.value > self.value:
            return numero.value
        return self.value
    
class Cadena:
    value = ""
    
    def __init__(self, value):
        self.value = value
        
    def comparar(self, cadena):
        palabras = [self.value, cadena.value]
        palabras.sort()
        return palabras[0]

class Lista:
    value = []
    
    def __init__(self, value):
        self.value = value
    
    def comparar(self, lista):
        if len(self.value) > len(lista.value):
            return self.value
        return lista.value
    
    
def retornaElMayor(a,b):
    return a.comparar(b)

numero_uno = Numero(10)
numero_dos = Numero(200)
print(retornaElMayor(numero_uno, numero_dos))

cadena_uno = Cadena("Jose")
cadena_dos = Cadena("Hector")
print(retornaElMayor(cadena_uno, cadena_dos))

lista_uno = Lista([1,2])
lista_dos = Lista([1,2,3,4,])
print(retornaElMayor(lista_uno, lista_dos))