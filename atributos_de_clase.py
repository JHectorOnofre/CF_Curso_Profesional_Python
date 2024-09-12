class Usuario:
    #atributos de clase:
    username = ""
    email = ""

Usuario.username = "Hector"
Usuario.email = "correo@correo.com"


user1 = Usuario() #Objeto de tipo usuario "user1"

user1.username = "hector" #se añade el atributo al objeto
user1.password = "12345"
print(user1.username)

print(id(user1))
print(id(Usuario.username))

user1.password = "new password"

print(user1.__dict__) #diccionario de atributos del objeto
