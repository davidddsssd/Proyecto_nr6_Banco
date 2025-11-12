#pip install -r requirements.txt

from iu.menu import menu_inicio
from iu.grafica import iniciar_interfaz

if __name__ == "__main__":
    try:
        print("\n¿Qué tipo de interfaz desea usar?")
        print("[1] Interfaz de Terminal")
        print("[2] Interfaz Gráfica")
        opcion = input("Opción: ").strip()
        
        if opcion == "1":
            menu_inicio()
        elif opcion == "2":
            iniciar_interfaz()
        else:
            print("Opción no válida. Iniciando en modo terminal por defecto...")
            menu_inicio()

    except KeyboardInterrupt:
        print("\n\nPrograma interrumpido por el usuario. Cerrando con seguridad...\n")

    except Exception as e:
        print(f"\nError inesperado al iniciar el sistema: {e}\n")