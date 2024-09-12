
direcciones = {
    "Elena":"Roma 123, Italia",
    "Pablo":"Paris 225A, Francia",
    "Josué":"Malaga 89, España"
}

#impirmir dirección con base en el nombre de la persona
print(direcciones["Elena"])


#Si una persona no se encuentra:
print(direcciones.get("Pedro", "Persona no se encuentra en el directorio"))


#con base a la dirección, a quién pertenece
direccion_buscada = "Malaga 80, España" #89, no 80


if(direccion_buscada in direcciones.values()):
    
    for persona, direccion in direcciones.items():
        if(direccion_buscada == direccion):
            print(persona)
else:
    print("No existe la direccion indicada")