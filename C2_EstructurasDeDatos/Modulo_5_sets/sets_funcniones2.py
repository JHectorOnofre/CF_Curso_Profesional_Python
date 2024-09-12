### union(), interesection(), isdisjoint, difference


set = {"Python", "Java", "JavaScript", "C#", "PHP"}
set2 = {"Swift", "Kotlin", "Dart", "JavaScript", "Java"}


#Union: unir 2 conjuntos
union = set.union(set2)
print(union)

#intersecion: indica los valores que hay en común
coincidencias = set.intersection(set2)
print(coincidencias)


#isdisjoint: devuelve True cuando no hay intersección (coincidencias)
interseccion = set.isdisjoint(set2)
print(interseccion) #false, ya que 2 si coinciden


#difference: devuelve todas las diferencias (del set1) respecto al 2 
diferentes = set.difference(set2)
print(diferentes) #elementos diferentes y que son del set1
