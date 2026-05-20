from archivo_json import cargar_json, guardar_json
from datetime import date

# Nombre del archivo donde se almacenan todos los gastos del sistema
ARCHIVO_GASTOS = "datos.json"


# =========================================================================
# REGISTRAR GASTO
# =========================================================================
def registrar_gasto(usuario):
    # Carga la lista actual de gastos desde el archivo JSON
    datos = cargar_json(ARCHIVO_GASTOS)

    # Solicita los datos del nuevo gasto al usuario por consola
    descripcion = input("Descripción del gasto: ")
    monto = float(input("Monto: "))
    #Agregamos la categoría requerida para el reporte del examen
    categoria = input("Categoría : ").strip().lower()

    #Estructura del diccionario que representa el gasto, ahora con 'categoria'
    gasto = {
        "usuario": usuario,
        "fecha": str(date.today()), # Guarda la fecha actual en formato YYYY-MM-DD
        "descripcion": descripcion,
        "monto": monto,
        "categoria": categoria # Guardamos la categoría en minúsculas para facilitar búsquedas
    }

    # Agrega el nuevo gasto al listado existente
    datos.append(gasto)
    # Guarda la lista actualizada en el archivo JSON
    guardar_json(ARCHIVO_GASTOS, datos)

    print(" Gasto registrado con éxito")


# =========================================================================
# VER GASTOS
# =========================================================================
def ver_gastos(usuario):
    # Carga todos los gastos del sistema
    datos = cargar_json(ARCHIVO_GASTOS)

    # Filtra los gastos para mostrar únicamente los que pertenecen al usuario logueado
    filtrados = [g for g in datos if g["usuario"] == usuario]

    # Si el usuario no tiene gastos, avisa y corta la ejecución de la función
    if not filtrados:
        print("No tienes gastos registrados")
        return

    print("\n Tus gastos:")
    # Recorre y muestra en pantalla cada uno de los gastos filtrados
    for g in filtrados:
        # ETIQUETA: Se añade la visualización de la categoría en el print de consola
        categoria_str = g.get('categoria', 'Sin categoría')
        print(f"{g['fecha']} - [{categoria_str.capitalize()}] {g['descripcion']} - ${g['monto']}")


# =========================================================================
# TOTAL GASTADO
# =========================================================================
def total_gastado(usuario):
    # Carga todos los gastos del sistema
    datos = cargar_json(ARCHIVO_GASTOS)

    # Suma el monto de todos los gastos que coincidan con el usuario actual
    total = sum(g["monto"] for g in datos if g["usuario"] == usuario)

    print(f"\n Total gastado: ${total}")