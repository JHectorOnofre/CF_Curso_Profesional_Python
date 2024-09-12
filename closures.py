'''la función saludar es un closure, retorna otra función 
que puede accdeder a las variables locales, aun cuando saludar
ha finalizado
'''
def saludar(username): 
    mensaje = f"Hola {username}" #variable local mensaje
    
    def mostrar_mensaje(): #función anidada
        print(mensaje)
        
    return mostrar_mensaje

username = "Hector"
respuesta = saludar(username)

username = "Jose" #no se muestra actualizada
'''
La función seguirá saludando a Hector, ya que es el valor que 
tenía username al momento de ejecutarse la función
'''

respuesta()
respuesta()
respuesta()