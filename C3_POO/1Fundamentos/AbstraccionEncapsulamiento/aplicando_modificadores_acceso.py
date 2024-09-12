class Usuario: #Clase Padre
    
    def __init__(self, parametro_nombre): #Método constructor
        self._nombre = parametro_nombre #Protected
    
    def saludar(self, saludo):
        print(saludo + self.nombre)


class Empleado(Usuario): #Clase Hija
    __salario = 0
    
    #Métodos específicos de la clase Hija
    def modificar_salario(self, salario):
        self.__salario = salario
    
    def ver_salario(self):
        print(self.__salario)
        
    def saludar(self):
        super().saludar("Hola desde el método Empleado ! ")  
        #print("Mi nombres es:" +self.nombre+" y gano:"+str(self.salario))

nombre_empleado = Empleado("Hector")
print(nombre_empleado._Empleado__salario) # se accede a una propiedad "privada"
