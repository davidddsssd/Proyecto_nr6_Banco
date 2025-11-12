#pip install -r requirements.txt

from iu.menu import menu_inicio
from iu.grafica import iniciar_interfaz

if __name__ == "__main__":
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