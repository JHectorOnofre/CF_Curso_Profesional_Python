class Usuario: #Clase Padre
    
    def __init__(self, parametro_nombre): #Método constructor
        self.nombre = parametro_nombre
    
    def saludar(self, saludo):
        print(saludo + self.nombre)


class Empleado(Usuario): #Clase Hija
    salario = 0
    
    #Métodos específicos de la clase Hija
    def modificar_salario(self, salario):
        self.salario = salario
    
    def ver_salario(self):
        print(self.salario)
        
    def saludar(self):
        super().saludar("Hola desde el método Empleado ! ")  
        #print("Mi nombres es:" +self.nombre+" y gano:"+str(self.salario))

nombre_empleado = Empleado("Hector")
nombre_empleado.saludar()


### Ejemplo 2 clase super
class Pagina: #Clase 
    def imprimir_pie_pagina(self): #metodo
        print(self.pie_pagina)
    
class PaginaLegal(Pagina): #especialización de la clase
    def imprimir_pie_pagina(self): #extiende la funcionalidad del método de la L29
        super().imprimir_pie_pagina() 
        print("Derechos reservados")
