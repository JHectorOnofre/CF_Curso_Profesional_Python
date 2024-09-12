from abc import ABC, abstractmethod

class EstructuraAbstracta(ABC): #Máxima abstraccion
    
    @abstractmethod
    def obtener():
        pass
    
    @abstractmethod
    def agregar():
        pass

#Siguiente nivel de abstracción, hay implementación pero no lógica de negocio
class Hash(EstructuraAbstracta):
    datos = {}
    
    def obtener(self, llave):
        datos[llave]
        
    def agregar(self, llave, valor):
        datos[llave] = valor
        

class Queue(EstructuraAbstracta):
    
    datos = []
    
    def obtener(self):
        datos[0]
        
    def agregar(self, llave, valor):
        datos[len(datos)-1] = valor
        
#Tercer nivel de abstracción en el cual ya hay vocabulario como banco, usuarios, filas
class FilaBanco:
    usuarios = Queue()
    
    def __init__(self, almacen_usuarios):
        if not isinstance(almacen_usuarios, EstructuraAbstracta):
            raise ValueError("Store is not supported")

        self.usuarios = almacen_usuarios
    
    def siguiente_usaurio(self, numero):
        return self.usuarios.obtener(numero)
        #implementación
        pass
    
    def formar_usuario(self, numero, usuario):
        self.usuario.agregar(numero, usuario)
        
FilaBanco([])