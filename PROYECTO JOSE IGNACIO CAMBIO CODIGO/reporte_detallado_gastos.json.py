import os
import json
from datetime import datetime
from archivo_json import cargar_json

# =========================================================================
# FUNCIÓN PRINCIPAL DE REPORTES 
# =========================================================================
#none es como un marcador de posición para inicializar variables vacías
def reporte_detallado(fecha_inicio, fecha_fin, categoria_opcional=None):  
    
    #Intenta validar que las fechas tengan el formato correcto
    try:
        #Convierte la fecha de inicio de texto a objeto de fecha
        f_desde = datetime.strptime(fecha_inicio, "%Y-%m-%d").date()
        #Convierte la fecha de fin de texto a objeto de fecha
        f_hasta = datetime.strptime(fecha_fin, "%Y-%m-%d").date()
    #Si el usuario escribió mal la fecha, atrapa el error
    except ValueError:
        #Muestra mensaje de error en la consola
        print(" Error: Formato de fecha inválido (Debe ser YYYY-MM-DD)")
        #Detiene la función por completo
        return

    #Carga todos los gastos desde el archivo JSON principal
    todos = cargar_json("datos.json")
    
    #Crea una lista vacía para guardar los gastos que cumplan los filtros
    filtrados = []
    
    #Bucle abajo para revisar uno por uno todos los gastos cargados
    for g in todos:
        #Convierte la fecha del gasto actual a objeto de fecha para comparar
        f_gasto = datetime.strptime(g["fecha"], "%Y-%m-%d").date()
        
        #Evalúa si la fecha del gasto está dentro del rango solicitado
        en_rango = f_desde <= f_gasto <= f_hasta
        
        #Verifica si no se pidió categoría O si la del gasto coincide con la buscada
        mismo_cat = not categoria_opcional or g.get("categoria", "").lower() == categoria_opcional.lower()
        
        #Si el gasto cumple con la fecha y con la categoría...
        if en_rango and mismo_cat:
            #Agrega este gasto a nuestra lista de resultados filtrados
            filtrados.append(g)

    #Inicializa el acumulador del dinero total gastado en 0
    total_general = 0.0
    #Crea un diccionario vacío para guardar los totales por cada categoría
    totales_por_cat = {}

    #Bucle abajo para calcular los totales usando la lista ya filtrada
    for g in filtrados:
        #Extrae el monto del gasto actual y lo convierte a número decimal
        monto = float(g["monto"])
        #Suma el monto al total 
        total_general += monto
        
        #Obtiene la categoría del gasto actual
        cat = g.get("categoria", "sin categoria").lower()
        #Si la categoría no existía en el diccionario de totales, la crea en 0
        if cat not in totales_por_cat:
            totales_por_cat[cat] = 0.0
        #suma el monto al subtotal específico de esa categoría
        totales_por_cat[cat] += monto

    #Crea la lista de gastos limpia 
    lista_limpia = []
    #Bucle para formatear los gastos filtrados
    for g in filtrados:
        #Agrega al arreglo el diccionario con las 4 llaves qu me piden
        lista_limpia.append({
            "fecha": g["fecha"],
            "categoria": g.get("categoria", "sin categoria"),
            "monto": g["monto"],
            "descripcion": g["descripcion"]
        })

    #Construye la estructura final del reporte JSON
    reporte_json = {
        "rango_fechas_consultado": {"inicio": fecha_inicio, "fin": fecha_fin},
        "categoria_consultada": categoria_opcional if categoria_opcional else "todas",
        "lista_de_gastos": lista_limpia,
        "totales": {"total_general": total_general, "total_por_categoria": totales_por_cat}
    }

    #Comprueba si la carpeta reports no existe
    if not os.path.exists("reports"):
        #Crea la carpeta reports de forma automática
        os.makedirs("reports")
        
    #Define la ruta completa donde se guardará el archivo JSON
    ruta = os.path.join("reports", "reporte_detailed_gastos.json")
    
    #Abre el archivo JSON en modo escritura ("w")
    with open(ruta, "w", encoding="utf-8") as f:
        #Guarda los datos estructurados y los indenta con 4 espacios
        json.dump(reporte_json, f, indent=4, ensure_ascii=False)

    #Verifica si la lista de gastos filtrados se quedó vacía
    if not filtrados:
        #Muestra el aviso obligatorio de que no se encontraron datos en el rango
        print("\n Alerta: No hay gastos en este rango. Archivo vacío creado.")

    #Imprime el encabezado del resumen en la terminal
    print("\n===== RESUMEN =====")
    #Muestra cuántos gastos se encontraron en total
    print(f"Gastos encontrados: {len(filtrados)}")
    #Muestra la suma total del dinero gastado
    print(f"Total general: ${total_general}")
    #Confirma la ubicación exacta donde se guardó el reporte
    print(f"Guardado en: {ruta}")    