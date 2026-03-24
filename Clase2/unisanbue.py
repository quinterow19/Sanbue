import random
import string
import time
import json
import os

ARCHIVO = "password_data.json"

# Generar contraseña aleatoria de 10 caracteres
def generar_contraseña():
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(caracteres) for _ in range(10))

# Guardar contraseña y timestamp
def guardar_contraseña(password):
    data = {
        "password": password,
        "timestamp": time.time()
    }
    with open(ARCHIVO, "w") as f:
        json.dump(data, f)

# Cargar contraseña
def cargar_contraseña():
    if not os.path.exists(ARCHIVO):
        return None
    with open(ARCHIVO, "r") as f:
        return json.load(f)

# Verificar si han pasado 24 horas (86400 segundos)
def necesita_cambio(timestamp):
    return (time.time() - timestamp) > 86400

# Obtener contraseña actual (y regenerar si es necesario)
def obtener_contraseña_actual():
    data = cargar_contraseña()

    if data is None or necesita_cambio(data["timestamp"]):
        nueva_password = generar_contraseña()
        guardar_contraseña(nueva_password)
        print("🔄 Nueva contraseña generada:", nueva_password)
        return nueva_password
    else:
        return data["password"]

# Validar contraseña ingresada por el usuario
def validar_contraseña(input_usuario):
    password_actual = obtener_contraseña_actual()
    if input_usuario == password_actual:
        print("✅ Contraseña correcta")
    else:
        print("❌ Contraseña incorrecta")

# ------------------ PROGRAMA PRINCIPAL ------------------

if __name__ == "__main__":
    print("Sistema de validación de contraseñas")

    # Mostrar contraseña actual (solo para pruebas, puedes quitar esto)
    contraseña_actual = obtener_contraseña_actual()
    print("Contraseña actual (debug):", contraseña_actual)

    intento = input("Ingresa la contraseña: ")
    validar_contraseña(intento)