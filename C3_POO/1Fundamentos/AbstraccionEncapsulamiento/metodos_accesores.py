class Usuario: 
    __edad = 0
    
    def __init__(self, parametro_nombre): #Método constructor
        self._nombre = parametro_nombre #Protected
    
    def saludar(self, saludo):
        print(saludo + self.nombre)

    @property
    def edad(self): #getter
        return self.__edad
    
    @edad.setter 
    def edad(self,valor):
        if(valor < 0):
            raise ValueError("Edad no puede ser menor que 0")
        self.__edad = valor


class Empleado(Usuario): #Clase Hija
    __salario = 0
    
    def modificar_salario(self, salario): #Setter: asigna valor a propiedad salario
        self.__salario = salario
    
    def ver_salario(self): #Getter: obtiene el valor actual de la propiedad
        print(self.__salario)
        
    def saludar(self):
        super().saludar("Hola desde el método Empleado ! ")  
        #print("Mi nombres es:" +self.nombre+" y gano:"+str(self.salario))

nombre_empleado = Empleado("Hector")
#print(nombre_empleado._Empleado__salario)
nombre_empleado.edad = -1 #Validación de la edad debe ser > 0
print(nombre_empleado.edad)