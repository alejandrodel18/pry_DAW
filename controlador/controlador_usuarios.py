from bd import obtener_conexion

def insertar_usuario(usuario_tipo_id, usu_nombre, usu_apellidos, usu_email, usu_clave, usu_dni):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO usuario(usuario_tipo_id, usu_nombre, usu_apellidos, usu_email, usu_clave, usu_dni) VALUES (%s, %s, %s, %s, %s, %s)",
                       (usuario_tipo_id, usu_nombre, usu_apellidos, usu_email, usu_clave, usu_dni))
    conexion.commit()
    conexion.close()


def obtener_usuarios():
    conexion = obtener_conexion()
    usuarios = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT usuario_id, usuario_tipo_id, usu_nombre, usu_apellidos, usu_email, usu_clave, usu_dni FROM usuario")
        usuarios = cursor.fetchall()
    conexion.close()
    return usuarios


def eliminar_usuario(usuario_id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM usuario WHERE usuario_id = %s", (usuario_id,))
    conexion.commit()
    conexion.close()


def obtener_usuario_por_id(usuario_id):
    conexion = obtener_conexion()
    juego = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT usuario_id, usuario_tipo_id, usu_nombre, usu_apellidos, usu_email, usu_clave, usu_dni FROM usuario WHERE usuario_id = %s", (usuario_id,))
        juego = cursor.fetchone()
    conexion.close()
    return juego


def actualizar_usuario(usuario_tipo_id, usu_nombre, usu_apellidos, usu_email, usu_clave, usu_dni, usuario_id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE usuario SET usuario_tipo_id = %s, usu_nombre = %s, usu_apellidos = %s, usu_email = %s, usu_clave = %s, usu_dni = %s WHERE usuario_id = %s",
                       (usuario_tipo_id, usu_nombre, usu_apellidos, usu_email, usu_clave, usu_dni, usuario_id))
    conexion.commit()
    conexion.close()
