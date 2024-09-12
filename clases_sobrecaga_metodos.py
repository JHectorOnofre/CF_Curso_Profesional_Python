class Animal:
    
    def comer(self):
       print("el animal come")
       
    def dormir(self):
        print("el animal duerme")


class Mascota(Animal):
    
    def comer(self):
        super().comer()
        print("la mascota come")


class Felino:
    def cazar(self):
        print("el felino caza")


class Gato(Mascota, Felino):
    
    def __init__(self, nombre):
        self.nombre = nombre
        
    def comer(self):
        super().comer() #acceder al método de la clase padre más inmediata
        print(f'{self.nombre} come')
    
    def dormir(self):
        print(f'{self.nombre} duerme ')

mei = Gato("Mei") #se crea el objeto Gato con un nombre

#se ejecutan los métodos comer y dormir
mei.comer()
mei.dormir()
