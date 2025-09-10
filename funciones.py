from random import shuffle
#
#
def cargar_configuracion():
    with open("configuracion.txt", "r", encoding="utf-8") as archivo:
        lineas = archivo.readlines()

    lista = []
    for elemento in lineas:
        elemento = elemento.strip()
        if elemento:
            lista.append(elemento)
    return lista
##
##
def configurar_juego():
    print("funcion para configurar la lista de animales")
    respuesta = input("preguntar si desea configurar o cargar configuracion")
    if respuesta.lower == "cargar":
        return cargar_configuracion()

    animales = []
    while True:
        animal = input("cual es el animal")
        if animal.lower() == "q":
            exit()
        elif animal.lower() == "jugar":
            break
        else:
            animales.append(animal)
    return animales

def elegir_animal(animales):
    print("funcion para que el ordenador elija el animal")
    shuffle(animales)
    return animales[0]
#
#
def adivinar(animales):
    print("funcion para adivinar el animal elegido por la compu")
    elegido = elegir_animal(animales)
    print("\nHora de adivinar")
    print("\nanimal que e elegido", animales)
    print("escribe q para salir en cualquier momento \n")

    while True:
        intento = input("que animal crees que elegi")
        if intento.lower() == "q":
         exit()
        elif intento.lower() == elegido.lower():
         print("has ganado")
        break
    else:
        print("No as acertado. Intenta de nuevo.")

## Este bloque permite usar funciones sin que se ejecute el juego automáticamente si lo importas
if __name__ == "__main__":
    animales = configurar_juego()
    adivinar(animales)
