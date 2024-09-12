'''
a = función princial (decorador)
b = función de decorar (argumento)
c = funcón decorada (función anidada)

La función "a", recibe a la "b" como argumento y darán como 
resulado a la función "c": a(b) -> c
'''

#Estructura base de un decorador
def function_a(function_b):
    
    def function_c():
        print(">>> antes del llamado")
        
        function_b()
        
        print(">>> despues  del llamado")
    
    return function_c #retorno de la function a

@function_a 
def saludar():
    print("Hola, esta es una función")
    
    
@function_a
def suma():
    print(10 + 30)

suma()
