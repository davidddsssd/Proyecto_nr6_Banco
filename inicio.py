#pip install -r requirements.txt

if __name__ == "__main__":
    # Importar de forma perezosa (cuando ya sabemos qué interfaz usar)
    print("\n¿Qué tipo de interfaz desea usar?")
    print("[1] Interfaz de Terminal")
    print("[2] Interfaz Gráfica")
    opcion = input("Opción: ").strip()

    if opcion == "1":
        from iu.menu import menu_inicio
        menu_inicio()
    elif opcion == "2":
        from iu.grafica import iniciar_interfaz
        iniciar_interfaz()
    else:
        print("Opción no válida. Iniciando en modo terminal por defecto...")
        from iu.menu import menu_inicio
        menu_inicio()

