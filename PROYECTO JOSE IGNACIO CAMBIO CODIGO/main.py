from usuarios import registrar_usuario, iniciar_sesion
from gastos import registrar_gasto, ver_gastos, total_gastado
#Importamos la nueva función de reportes detallados
from reportes import reporte_detallado


# =========================================================================
# MENÚ DE GASTOS 
# =========================================================================
def menu_finanzas(usuario):

    while True:
        print("\n===== APP FINANZAS =====")
        print("1. Registrar gasto")
        print("2. Ver gastos")
        print("3. Ver total gastado")
        print("4. Generar Reporte Detallado (nueva funvion)") # <---Nueva opción agregada
        print("5. Cerrar sesión")

        opcion = input("Seleccione: ")

        if opcion == "1":
            registrar_gasto(usuario)

        elif opcion == "2":
            ver_gastos(usuario)

        elif opcion == "3":
            total_gastado(usuario)

        elif opcion == "4":
            #CAPTURA DE PARÁMETROS DESDE LA CONSOLA
            print("\n--- GENERADOR DE REPORTES ---")
            f_inicio = input("Ingrese Fecha Inicio (YYYY-MM-DD): ").strip()
            f_fin = input("Ingrese Fecha Fin (YYYY-MM-DD): ").strip()
            cat_opc = input("Categoría específica (Opcional - Presione ENTER para saltar): ").strip()
            
            #Validar si el usuario omitió la categoría para mandar None o el texto
            if cat_opc == "":
                reporte_detallado(f_inicio, f_fin, categoria_opcional=None)
            else:
                reporte_detallado(f_inicio, f_fin, categoria_opcional=cat_opc)

        elif opcion == "5":
            print("Cerrando sesión...")
            break

        else:
            print(" Opción inválida")


# =========================================================================
# MENÚ PRINCIPAL (LOGIN Y REGISTRO)
# =========================================================================
def main():

    while True:
        print("\n===== BIENVENIDO A LA APP =====")
        print("1. Registrarse")
        print("2. Iniciar sesión")
        print("3. Salir")

        opcion = input("Elige: ")

        if opcion == "1":
            registrar_usuario()

        elif opcion == "2":
            usuario = iniciar_sesion()

            # Si las credenciales son válidas, da acceso al menú de finanzas
            if usuario:
                menu_finanzas(usuario)

        elif opcion == "3":
            print(" Adiós")
            break

        else:
            print(" Opción inválida")


#Disparador principal para iniciar la ejecución total del sistema
if __name__ == "__main__":
    main()