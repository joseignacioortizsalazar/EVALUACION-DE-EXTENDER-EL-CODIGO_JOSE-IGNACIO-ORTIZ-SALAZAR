import json
import os

# =========================
# ARCHIVO DE GASTOS
# =========================
ARCHIVO_GASTOS = "datos.json"
ARCHIVO_USUARIOS = "usuarios.json"


# =========================
# CARGAR JSON GENERICO
# =========================
def cargar_json(archivo):
    if os.path.exists(archivo):
        with open(archivo, "r") as file:
            return json.load(file)
    return []


# =========================
# GUARDAR JSON GENERICO
# =========================
def guardar_json(archivo, datos):
    with open(archivo, "w") as file:
        json.dump(datos, file, indent=4)