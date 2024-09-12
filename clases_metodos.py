class Usuario:
    pass #un bloque que no realiza ninguna acción por ahora

#usuario hector, no contiene atributos, no se colocan argumentos
hector = Usuario() 
print(hector)

#el objeto es de tipo Usuario


## Métodos
class Usuaria:
    
    def inicializar(self, username, password):
        #añadiendo atributos al objeto
        self.username = username
        self.password = password

user1 = Usuaria()
user2 = Usuaria()

user1.inicializar("user1", "password1")
user2.inicializar("user2", "password2")

print(user1.__dict__)
print(user2.__dict__)