class Mascota: #clase padre
    
    def comer(self):
        print("la mascota come")

    def dormir(sef):
        print("la mascota duerme")


class Perro(Mascota): #clase hija
    pass

class Gato(Mascota): #clase hija
    pass


#objeto de tipo Perro, la cual hereda métodos y atribs de la 
#clase mascota
duke = Perro()

duke.comer()
duke.dormir()

michi = Gato()

michi.comer()
michi.dormir()