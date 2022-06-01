<head>
  <style type="text/css">
    body {
      padding-left: 11em;
      padding-right: 11em;
        }
  </style>
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
  <script data-require="bootstrap@3.1.1" data-semver="3.1.1" src="//netdna.bootstrapcdn.com/bootstrap/3.1.1/js/bootstrap.min.js"></script>
  <script data-require="marked@*" data-semver="0.3.1" src="http://cdnjs.cloudflare.com/ajax/libs/marked/0.3.1/marked.js"></script>
  <script src="https://cdn.rawgit.com/toopay/bootstrap-markdown/master/js/bootstrap-markdown.js
"></script>
  <script src="https://rawgit.com/lodev09/jquery-filedrop/master/jquery.filedrop.js
"></script>
  <script src="https://rawgit.com/jeresig/jquery.hotkeys/master/jquery.hotkeys.js"></script>
  <link data-require="bootstrap-css@3.1.1" data-semver="3.1.1" rel="stylesheet" href="//netdna.bootstrapcdn.com/bootstrap/3.1.1/css/bootstrap.min.css" />
  <link data-require="fontawesome@4.1.0" data-semver="4.1.0" rel="stylesheet" href="//netdna.bootstrapcdn.com/font-awesome/4.1.0/css/font-awesome.min.css" />
  <link rel="stylesheet" href="https://cdn.rawgit.com/toopay/bootstrap-markdown/master/css/bootstrap-markdown.min.css" />
</head>

# API - DOCUMENTATION
***

## USUARIO

### Obtener Usuarios
  1. Metodo (**GET**)
  2. URL: [https://bd-pryfinaldaw1.herokuapp.com/api/obtener_usuarios](https://bd-pryfinaldaw1.herokuapp.com/api/obtener_usuarios)

### Obtener Usuario x ID
  1. Metodo (**GET**)
  2. URL: [https://bd-pryfinaldaw1.herokuapp.com/api/obtener_usuario/{id}](https://bd-pryfinaldaw1.herokuapp.com/api/obtener_usuario/4)

### Agregar Usuario
  1. Metodo (**POST**)
  2. URL: [https://bd-pryfinaldaw1.herokuapp.com/api/guardar_usuario](https://bd-pryfinaldaw1.herokuapp.com/api/guardar_usuario)
  3. BODY:
````
{
  "tipo":1,
  "usu_nombre":"xdxdxdxd",
  "apellidos":"xdxdxdxd",
  "email":"xdxdxdxd",
  "clave":"xdxdxdxd",
  "dni":"xdxdxdxd"
}
````

### Modificar Usuario
  1. Metodo (**POST**)
  2. URL: [https://bd-pryfinaldaw1.herokuapp.com/api/guardar_usuario](https://bd-pryfinaldaw1.herokuapp.com/api/guardar_usuario)
  3. BODY:
````
{
  "id": 22
  "tipo":1,
  "usu_nombre":"prueba",
  "apellidos":"prueba",
  "email":"prueba",
  "clave":"prueba",
  "dni":"prueba"
}
````

### Eliminar Usuario
  1. Metodo (**POST**)
  2. URL: [https://bd-pryfinaldaw1.herokuapp.com/api/eliminar_usuario](https://bd-pryfinaldaw1.herokuapp.com/api/eliminar_usuario)
  3. BODY:
````
{
  "id": 22
}
````
***
## TIPO_USUARIO

### Obtener Tipo_Usuarios
  1. Metodo (**GET**)
  2. URL: [https://bd-pryfinaldaw1.herokuapp.com/api/obtener_tipo_usuarios](https://bd-pryfinaldaw1.herokuapp.com/api/obtener_tipo_usuarios)

### Obtener Usuario x ID
  1. Metodo (**GET**)
  2. URL: [https://bd-pryfinaldaw1.herokuapp.com/api/obtener_tipo_usuario/{id}](https://bd-pryfinaldaw1.herokuapp.com/api/obtener_tipo_usuario/3)

### Agregar Tipo Usuario
  1. Metodo (**POST**)
  2. URL: [https://bd-pryfinaldaw1.herokuapp.com/api/guardar_tipo_usuario](https://bd-pryfinaldaw1.herokuapp.com/api/guardar_tipo_usuario)
  3. BODY:
````
{
  "nombre": "hola",
  "descripcion":"hola"
}
````

### Modificar Tipo Usuario
  1. Metodo (**POST**)
  2. URL: [https://bd-pryfinaldaw1.herokuapp.com/api/actualizar_tipo_usuario](https://bd-pryfinaldaw1.herokuapp.com/api/actualizar_tipo_usuario)
  3. BODY:
````
{
  "usuario_tipo_id":"15",
  "ut_nombre":"prueba123",
  "ut_descripcion":"prueba123"
}
````

### Eliminar Tipo Usuario
  1. Metodo (**POST**)
  2. URL: [https://bd-pryfinaldaw1.herokuapp.com/api/eliminar_tipousuario](https://bd-pryfinaldaw1.herokuapp.com/api/eliminar_tipousuario)
  3. BODY:
````
{
  "usuario_tipo_id": 22
}
````
