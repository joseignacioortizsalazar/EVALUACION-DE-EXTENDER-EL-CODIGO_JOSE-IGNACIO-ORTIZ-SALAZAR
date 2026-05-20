from archivo_json import cargar_json, guardar_json

ARCHIVO_USUARIOS = "usuarios.json"


# =========================
# REGISTRAR USUARIO
# =========================
def registrar_usuario():
    usuarios = cargar_json(ARCHIVO_USUARIOS)

    user = input("Nuevo usuario: ")
    password = input("Nueva contraseña: ")

    # verificar si existe
    for u in usuarios:
        if u["usuario"] == user:
            print(" Usuario ya existe")
            return False

    usuarios.append({
        "usuario": user,
        "password": password
    })

    guardar_json(ARCHIVO_USUARIOS, usuarios)
    print(" Usuario creado")
    return True


# =========================
# LOGIN
# =========================
def iniciar_sesion():
    usuarios = cargar_json(ARCHIVO_USUARIOS)

    user = input("Usuario: ")
    password = input("Contraseña: ")

    for u in usuarios:
        if u["usuario"] == user and u["password"] == password:
            print(f" Bienvenido {user}")
            return user

    print("❌ Usuario o contraseña incorrectos")
    return None