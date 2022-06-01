from bd import obtener_conexion

def insertar_tipo_usuario(ut_nombre, ut_descripcion):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO usuario_tipo(ut_nombre, ut_descripcion) VALUES (%s, %s)",
                       (ut_nombre, ut_descripcion))
    conexion.commit()
    conexion.close()


def obtener_tipos_usuario():
    conexion = obtener_conexion()
    tipos_usuarios = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT usuario_tipo_id, ut_nombre, ut_descripcion FROM usuario_tipo")
        tipos_usuarios = cursor.fetchall()
    conexion.close()
    return tipos_usuarios


def eliminar_tipoUsuario(usuario_tipo_id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM usuario_tipo WHERE usuario_tipo_id = %s", (usuario_tipo_id,))
    conexion.commit()
    conexion.close()


def obtener_tipo_usuario_por_id(usuario_tipo_id):
    conexion = obtener_conexion()
    juego = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT usuario_tipo_id, ut_nombre, ut_descripcion FROM usuario_tipo WHERE usuario_tipo_id = %s", (usuario_tipo_id,))
        juego = cursor.fetchone()
    conexion.close()
    return juego

def actualizar_tipoUsuario(ut_nombre, ut_descripcion,usuario_tipo_id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE usuario_tipo SET ut_nombre = %s, ut_descripcion = %s WHERE usuario_tipo_id = %s",
                       (ut_nombre, ut_descripcion, usuario_tipo_id))
    conexion.commit()
    conexion.close()
  

