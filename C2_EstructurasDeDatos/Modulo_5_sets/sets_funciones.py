## funciones add(), remove(), pop()
'''
A pesar de que los elementos dentro de un set no pueden ser 
modificados, si pueden agregarse y quitarse por funciones
'''

set_letras = {"a", "b", "c", "d", "e"}
print(set_letras)

#add() agregar elementos
set_letras.add("f")
print(set_letras)


#remove() eliminar elemento específico
set_letras.remove("c")
print(f"elimonamos latra 'c': {set_letras}")


#pop() elimina un elmeento aleatorio (no hay un último definido)
set_letras.pop()
print(set_letras)