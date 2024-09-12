'''
Estructura que permite almacenar datos por medio de llaves y valores
sintaxis clave:valor
Símil de un objeto en JS y de un hashing en Java
* sin indexados, se puede acceder a sus elementos por medio de su índice (llave)
* son dinámicos (no tienen un tamaño definido) 
* mutables (podemos modificar elementos dinámicamente)
* puede contener cualqueir tipo de valor: elemtos, listas, tuplasy diccionarios
'''

estudiante = {
    "nombre":"Hector",
    "apellido":"Onofre",
    "ciudad":"México"
}

print(estudiante["nombre"]) #impime el valor de la llave nombre

estudiante["edad"] = 25 #agreaga una llave y valor
print(estudiante)

estudiante["edad"] = 26 #modifica el valor de la llave
print(estudiante)

estudiante["cursos"] = ["Python", "Java", "C#"]
print(estudiante)