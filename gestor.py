def guardar_contraseña():
    servicio = input("¿Para qué es? (Ej: Gmail): ")
    usuario = input("Usuario/Email: ")
    contraseña = input("Contraseña: ")
    
    with open("contraseñas.txt", "a") as archivo:
        archivo.write(f"{servicio} | {usuario} | {contraseña}\n")
    print("✅ ¡Contraseña guardada en 'contraseñas.txt'!")

def ver_contraseñas():
    try:
        with open("contraseñas.txt", "r") as archivo:
            print("\n🔐 TUS CONTRASEÑAS 🔐")
            print(archivo.read())
    except FileNotFoundError:
        print("❌ Aún no hay contraseñas guardadas.")

print("⚡ El programa ha iniciado correctamente ⚡")  # Mensaje de prueba

while True:
    print("\n-- MENÚ --")
    print("1. Guardar nueva contraseña")
    print("2. Ver todas las contraseñas")
    print("3. Salir")
    
    opcion = input("Elige una opción (1/2/3): ")
    
    if opcion == "1":
        guardar_contraseña()
    elif opcion == "2":
        ver_contraseñas()
    elif opcion == "3":
        print("¡Hasta luego! 👋")
        break
    else:
        print("❌ Opción no válida")

input("\nPresiona Enter para salir...")  # Evita que se cierre en Windows