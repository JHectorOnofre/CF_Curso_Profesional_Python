#nombre_variable [elementos]

lista = ["a", "b", "c"] #mismo tipo de dato

lista_distinta = ["A", 15, 2.75, True] #distintos tiops de datos

print(lista_distinta[0]) #imprime el primer elemento


#sublista
lista_principal = ["Java", "JavaScript", "Python", "Dart", "Cobol", "C#"]

sublista = lista_principal[0:3] #elementos 1[0], 2[1] y 3[2]


#Funciones
lista_principal.append("C++") #agregar elemento al final de la lista
print(lista_principal)

lista_principal.extend(["Elixir", "C", "F#", "VisualBasic"]) #agregar esta sublista
print(lista_principal)

lista_principal.insert(1, "Assembly") #agregar elemento en indice especificado
print(lista_principal)

lista_principal.remove("VisualBasic") #quitar elemento específico
print(lista_principal)

lista_principal.pop() #quitar último elemento actual
print(lista_principal)

lista_principal.pop(1) #quitar elemento 1
print(lista_principal)


#
print(lista_principal.count("JavaScript")) #num de veces que coincide 

print(lista_principal.index("Python")) #encontrar un item específico

print(len(lista_principal)) #cantidad elementos en lista principal
