
def function_a(function_b):
    
    def function_c(*args, **kwargs):
        print(">>> antes del llamado")
        
        resultado = function_b(*args, **kwargs)
        
        print(">>> despues  del llamado")
        
        return resultado
    
    return function_c #retorno de la function a

@function_a 
def saludar():
    print("Hola, esta es una función")
    
    
@function_a #la funcińo ahroa contiene parámetros
def suma(numero_1, numero2):
    return numero_1 + numero2 #la función ahora retorna un valor

resultado = suma(15, 41) #argumentos que requiere
print(resultado)