'''
Lista de alumnos, cuya información de cada uno es un diccionario,
uno de los elementos del diccionario es una lista de cursos
'''


lista_alumnos = [
    {"nombre": "Elena", "apellido":"Valdez", "id":123, "cursos":["Python", "Flask", "Git"]},
    {"nombre": "Juana", "apellido":"de Arco", "id":234, "cursos":["Fundamentos Web", "JavaScript"]},
    {"nombre": "Pedro", "apellido":"Lopez", "id":744, "cursos":["Fundamentos Cloud", "Azure","C"]}
]


#Eliminar curso de C de los cursos de Pedro:

lista_alumnos[2]["cursos"].remove("C")
# lista_alumnos[2]["cursos"].pop(2) -> Otra forma de hacerlo
print(lista_alumnos[2])
