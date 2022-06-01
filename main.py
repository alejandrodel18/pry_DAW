from flask import Flask, render_template, request, redirect, flash, jsonify

#from flaskext.markdown import Markdown

import markdown.extensions.fenced_code

#import Usuario as usu

#import tipo_usuario

import controlador.controlador_usuarios as controlador_usuarios                        
import controlador.controlador_tipo_usuario as controlador_tipo_usuario

app = Flask(__name__)

#--------------------------USUARIO------------------------

@app.route("/")
@app.route("/usuarios")
def usuarios():
    usuarios = controlador_usuarios.obtener_usuarios()
    return render_template("usuario/usuarios.html", usuarios=usuarios)

@app.route("/agregar_usuario")
def formulario_agregar_usuario():
    return render_template("usuario/agregar_usuario.html")

@app.route("/guardar_usuario", methods=["POST"])
def guardar_usuario():
    usuario_tipo_id = request.form["tipo"]
    usu_nombre = request.form["usu_nombre"]
    usu_apellidos = request.form["apellidos"]
    usu_email= request.form["email"]
    usu_clave = request.form["clave"]
    usu_dni = request.form["dni"]
    controlador_usuarios.insertar_usuario(usuario_tipo_id, usu_nombre, usu_apellidos, usu_email, usu_clave, usu_dni)
    # De cualquier modo, y si todo fue bien, redireccionar
    return redirect("/usuarios")

@app.route("/eliminar_usuarios", methods=["POST"])
def eliminar_usuario():
    controlador_usuarios.eliminar_usuario(request.form["id"])
    return redirect("/usuarios")

@app.route("/formulario_editar_usuario/<int:usuario_id>")
def editar_usuario(usuario_id):
    # Obtener el Usuario por ID
    usuario = controlador_usuarios.obtener_usuario_por_id(usuario_id)
    return render_template("usuario/editar_usuario.html", usuario=usuario)

@app.route("/actualizar_usuario", methods=["POST"])
def actualizar_usuario():
    usuario_id = request.form["id"]
    usuario_tipo_id = request.form["tipo"]
    usu_nombre = request.form["nombre"]
    usu_apellidos = request.form["apellidos"]
    usu_email= request.form["email"]
    usu_clave = request.form["clave"]
    usu_dni = request.form["dni"]
    controlador_usuarios.actualizar_usuario(usuario_tipo_id, usu_nombre, usu_apellidos, usu_email, usu_clave, usu_dni, usuario_id)
    return redirect("/usuarios")


#-----------------------API USUARIO -----------------------
@app.route("/api/obtener_usuarios")
def api_optenerusuarios():
  usuarios = controlador_usuarios.obtener_usuarios()
  
  return jsonify(usuarios)

@app.route("/api/obtener_usuario/<int:id>")
def api_obtenerusuarioid(id):
    usuario = controlador_usuarios.obtener_usuario_por_id(id)
    if(usuario is not None):
        return jsonify({"id":usuario[0],"tipo_id":usuario[1],"nombre":usuario[2],"apellido":usuario[3],"email":usuario[4],"clave":usuario[5],"dni":usuario[6]})
    return jsonify({"Mensaje": "Usuario no encontrado"})

@app.route("/api/guardar_usuario", methods=["POST"])
def api_guardar_usuario():
    #print(request.json["tokenid"])
    
    usuario_tipo_id = request.json["tipo"]
    usu_nombre = request.json["usu_nombre"]
    usu_apellidos = request.json["apellidos"]
    usu_email= request.json["email"]
    usu_clave = request.json["clave"]
    usu_dni = request.json["dni"]
    controlador_usuarios.insertar_usuario(usuario_tipo_id, usu_nombre, usu_apellidos, usu_email, usu_clave, usu_dni)
    # De cualquier modo, y si todo fue bien, redireccionar
    return jsonify({"Usuario Nombre":usu_nombre,"Mensaje": "Usuario registrado correctamente"})


@app.route("/api/actualizar_usuario", methods=["POST"])
def api_actualizar_usuario():
    usuario_id = request.json["id"]
    usuario_tipo_id = request.json["tipo"]
    usu_nombre = request.json["nombre"]
    usu_apellidos = request.json["apellidos"]
    usu_email= request.json["email"]
    usu_clave = request.json["clave"]
    usu_dni = request.json["dni"]
  
    validar_usuario = controlador_usuarios.obtener_usuario_por_id(usuario_id)

    if(validar_usuario is not None):
      controlador_usuarios.actualizar_usuario(usuario_tipo_id, usu_nombre, usu_apellidos, usu_email, usu_clave, usu_dni, usuario_id)
      return jsonify({"id":usuario_id,"nombre":usu_nombre,"Mensaje": "Usuario modificado correctamente"})
    return jsonify({"Mensaje": "Usuario no encontrado"})

  
@app.route("/api/eliminar_usuario", methods=["POST"])
def api_eliminar_Usuario():
  usuario_id = request.json["id"]
  
  validar_usuario = controlador_usuarios.obtener_usuario_por_id(usuario_id)

  if(validar_usuario is not None):
    controlador_usuarios.eliminar_usuario(usuario_id)
    return jsonify({"id":usuario_id ,"Mensaje": "Usuario eliminado correctamente"})
  return jsonify({"Mensaje": "Usuario no encontrado"})
  
#@app.route("/api/eliminar_usuario/<int:id>")
#def api_obtenerusuarioid(id):
#    usuario = controlador_usuarios.obtener_usuario_por_id(id)
#    if(usuario is not None):
#        return jsonify(usuario)
#    return jsonify({"Mensaje": "Usuario no encontrado"}) 




  
  
#--------------------------TIPO_USUARIO--------------------

@app.route("/tipos_usuarios")
def tipos_usuarios():
    tipos_usuarios = controlador_tipo_usuario.obtener_tipos_usuario()
    return render_template("tipos_usuario/tipos_usuarios.html", tipos_usuarios=tipos_usuarios)
  
@app.route("/agregar_tipos_usuarios")
def formulario_agregar_tipos_usuarios():
    return render_template("tipos_usuario/agregar_tipos_usuarios.html")

@app.route("/guardar_tipo_usuario", methods=["POST"])
def guardar_tipo_usuario():
    ut_nombre = request.form["ut_nombre"]
    ut_descripcion = request.form["ut_descripcion"]
  
    controlador_tipo_usuario.insertar_tipo_usuario(ut_nombre, ut_descripcion)
    # De cualquier modo, y si todo fue bien, redireccionar
    return redirect("/tipos_usuarios")


@app.route("/formulario_editar_tipos_usuarios/<int:usuario_tipo_id>")
def editar_tipos_usarios(usuario_tipo_id):
    # Obtener el Usuario por ID
    tipos_usuario = controlador_tipo_usuario.obtener_tipo_usuario_por_id(usuario_tipo_id)
    return render_template("tipos_usuario/editar_tipos_usuarios.html", tipos_usuario=tipos_usuario)


@app.route("/eliminar_tipoUsuario", methods=["POST"])
def eliminar_tipoUsuario():
    controlador_tipo_usuario.eliminar_tipoUsuario(request.form["id"])
    return redirect("/tipos_usuarios")

@app.route("/actualizar_tipoUsuario", methods=["POST"])
def actualizar_tipoUsuario():
    usuario_tipo_id = request.form["id"]
    ut_nombre = request.form["nombre"]
    ut_descripcion = request.form["descripcion"]
  
    controlador_tipo_usuario.actualizar_tipoUsuario(ut_nombre, ut_descripcion,usuario_tipo_id)
    return redirect("/tipos_usuarios")
  
#-----------------------API TIPO_USUARIO -----------------------
  
@app.route("/api/obtener_tipo_usuarios")
def api_optener_tipo_usuarios():
  tipo_usuarios = controlador_tipo_usuario.obtener_tipos_usuario()
  return jsonify(tipo_usuarios) 

@app.route("/api/obtener_tipo_usuario/<int:id>")
def api_optener_tipo_usuario(id):
    tipo_usuario = controlador_tipo_usuario.obtener_tipo_usuario_por_id(id)
    if(tipo_usuario is not None):
        return jsonify(tipo_usuario)
    return jsonify({"Mensaje": "Usuario no encontrado"})


@app.route("/api/guardar_tipo_usuario", methods=["POST"])
def api_guardar_tipo_usuario():
    #print(request.json["tokenid"]
    ut_nombre = request.json["nombre"]
    ut_descripcion = request.json["descripcion"]
    
    controlador_tipo_usuario.insertar_tipo_usuario(ut_nombre, ut_descripcion)

    return jsonify({"Usuario_Tipo TipoNombre":ut_nombre,"Mensaje": "Tipo de Usuario registrado correctamente"})


@app.route("/api/actualizar_tipo_usuario", methods=["POST"])
def api_actualizar_tipo_usuario():
    usuario_tipo_id = request.json["usuario_tipo_id"]
    ut_nombre = request.json["ut_nombre"]
    ut_descripcion = request.json["ut_descripcion"]
  
    validar_tipo_usuario = controlador_tipo_usuario.obtener_tipo_usuario_por_id(usuario_tipo_id)

    if(validar_tipo_usuario is not None):
      controlador_tipo_usuario.actualizar_tipoUsuario(ut_nombre, ut_descripcion,usuario_tipo_id)
      return jsonify({"id":usuario_tipo_id,"ut_nombre":ut_nombre,"Mensaje": "ipo usuario modificado correctamente"})
    return jsonify({"Mensaje": "Tipo Usuario no encontrado"})


@app.route("/api/eliminar_tipousuario", methods=["POST"])
def api_eliminar_tipoUsuario():
  id_tipoUsuario = request.json["usuario_tipo_id"]

  validar_id_tipoUsuario = controlador_tipo_usuario.obtener_tipo_usuario_por_id(id_tipoUsuario)

  if(validar_id_tipoUsuario is not None):
    controlador_tipo_usuario.eliminar_tipoUsuario(id_tipoUsuario)
    return jsonify({"id":id_tipoUsuario ,"Mensaje": "Tipo de Usuario eliminado correctamente"})
  return jsonify({"Mensaje": "tipo usuario no encontrado"})


#-------------------------------------------------------------------------------------


  
#------------------------MARKDOW-------------------------
@app.route("/readme")
def readme():
  readme_file = open("README.md", "r")
  md_template_string = markdown.markdown(
        readme_file.read(), extensions=["fenced_code"]
    )
  return md_template_string


# Iniciar el servidor
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
