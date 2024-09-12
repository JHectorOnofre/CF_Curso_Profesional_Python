promedio = lambda *args : sum(args) / len(args)

aprobatorio = lambda calificación : calificación >= 7


def mostrar_mensaje(func_promedio, func_aprobatorio, *args):
    promedio = func_promedio(*args)
    
    if func_aprobatorio(promedio):
        print(f"Felicidades, aprobaste con {promedio}")
    else: 
        print("No aprobaste la materia")

mostrar_mensaje(promedio, aprobatorio, 10, 10, 8 , 7)