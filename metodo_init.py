## Init

class Usuario:
    #objeto con parámetros con valores por default
    def __init__(self, username='', password=''): 
        self.username = username #atrib de instancia
        self.password = password

user1 = Usuario("user1", "pass1")
user2 = Usuario("user2", "pass2")

user3 = Usuario() #tendrá los valores por default

print(user1.__dict__) #para visualizar la asignación
print(user2.__dict__)
print(user3.__dict__)