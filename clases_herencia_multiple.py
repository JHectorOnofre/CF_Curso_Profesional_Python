class Animal:
    
    def comer(self):
       print("el animal come")
       
    def dormir(self):
        print("el animal duerme")


class Mascota(Animal):
    pass


class Felino:
    def cazar(self):
        print("el felino caza")


#Herencia múltiple, Gato hereda de Mascota y de Felino
class Gato(Mascota, Felino):
    pass

michi = Gato()

michi.comer()
michi.dormir()
michi.cazar() 
