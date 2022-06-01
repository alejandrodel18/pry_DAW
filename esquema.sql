CREATE TABLE usuario(
    usuario_id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    usuario_tipo_id INT(11) NOT NULL,
    usu_nombre VARCHAR(50) NOT NULL,
    usu_apellidos VARCHAR(50) NOT NULL,
    usu_email VARCHAR(50) NOT NULL,
    usu_clave VARCHAR(50) NOT NULL,
    usu_dni VARCHAR(10) NOT NULL
);

INSERT INTO usuario VALUES (1,1,'Cristhian','Sempertegui','csh@gmail.com','123456789','12345678');

INSERT INTO usuario VALUES (2,1,'Alex','Betancur','alex@gmail.com','123456789','12345678');

CREATE TABLE usuario_tipo(
    usuario_tipo_id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    ut_nombre VARCHAR(20) NOT NULL,
    ut_descripcion VARCHAR(200) NOT NULL
);

INSERT INTO usuario_tipo VALUES(1,'usuario1','Usuario Estandar');
INSERT INTO usuario_tipo VALUES(2,'usuario2','Usuario Bloqueado');
INSERT INTO usuario_tipo VALUES(3,'usuario3','Usuario Administrador');

CREATE TABLE tokends(
	tokenid VARCHAR(32),
	estado boolean
);
  
INSERT INTO tokends VALUES('vMGert*vpvX%hf9Ow7^m', true);
INSERT INTO tokends VALUES('aMt0CWTaPCr!Vz@36F9T', true);
INSERT INTO tokends VALUES('qzP#Lemrf@lxJEd4evWc', false);
INSERT INTO tokends VALUES('no&j0R97fEO!IpVOvOUG', false);