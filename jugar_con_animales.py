from funciones import configurar_juego, adivinar
#
#
def leer_instrucciones():
    with open("instrucciones.txt", "r", encoding="utf-8") as f:
        return f.read()

def main():  # 👈 corregido: antes decía manin
    print("=== JUGAR CON ANIMALES ===")

    # MOSTRAR INSTRUCCIONES DESDE ARCHIVO
    instrucciones = leer_instrucciones()  # 👈 corregido: era ==
    print(instrucciones)

    print("Agregar animales, cuando estés lista escribe 'jugar'.")
    animales = configurar_juego()
    adivinar(animales)

if __name__ == "__main__":
    main()