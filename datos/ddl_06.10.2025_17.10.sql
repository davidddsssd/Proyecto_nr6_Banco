USE proyecto_banco;

CREATE TABLE direccion IF NOT EXISTS(
    id_direccion INTEGER AUTO_INCREMENT,
    comuna VARCHAR(30) NOT NULL,
    calle VARCHAR(20) NOT NULL,
    departamento VARCHAR(20) NULL,
    numero_d VARCHAR(15) NOT NULL,

    CONSTRAINT pk_direccion PRIMARY KEY (id_direccion)
);

CREATE TABLE cliente IF NOT EXISTS(
    id_cliente INTEGER AUTO_INCREMENT,
    id_direccion INTEGER AUTO_INCREMENT,
    nombre VARCHAR(30) NOT NULL,
    apellido VARCHAR(30) NOT NULL,
    rut VARCHAR(12) NOT NULL,
    telefono INTEGER NOT NULL,
    mail VARCHAR(20) NULL,

    CONSTRAINT pk_cliente PRIMARY KEY (id_cliente),
    CONSTRAINT fk_direccion FOREIGN KEY (id_direccion) REFERENCES direccion(id_direccion)
);

CREATE TABLE cuenta IF NOT EXISTS(
    id_cliente INTEGER AUTO_INCREMENT,
    id_cuenta INTEGER AUTO_INCREMENT,
    numero_c VARCHAR(15) NOT NULL,
    saldo FLOAT NOT NULL,
    fecha_apertura DATETIME NOT NULL,
    tipo_cuenta BOOLEAN NOT NULL,
    estado_cuenta BOOLEAN NOT NULL,

    CONSTRAINT pk_cuenta PRIMARY KEY (id_cuenta),
    CONSTRAINT fk_cliente FOREIGN KEY (id_cliente) REFERENCES cliente(id_cliente)
);

CREATE TABLE cuenta_destino IF NOT EXISTS(
    id_cuenta_destino AUTO_INCREMENT INTEGER NOT NULL,
    tipo_cuenta VARCHAR(15) NOT NULL,
    estado_cuenta_destino BOOLEAN NOT NULL,

    CONSTRAINT pk_cuenta_destino PRIMARY KEY (id_cuenta_destino)
);

CREATE TABLE transaccion IF NOT EXISTS(
    id_cuenta INTEGER AUTO_INCREMENT,
    id_transaccion INTEGER AUTO_INCREMENT,
    id_cuenta_destino INTEGER AUTO_INCREMENT,
    tipo_transaccion VARCHAR(12) NOT NULL,
    fecha_transaccion DATETIME NOT NULL,
    monto FLOAT NOT NULL,

    CONSTRAINT pk_transaccion PRIMARY KEY (id_transaccion),
    CONSTRAINT fk_cuenta FOREIGN KEY (id_cuenta) REFERENCES cuenta(id_cuenta),
    CONSTRAINT fk_cuenta_destino FOREIGN KEY (id_cuenta_destino) REFERENCES cuenta_destino(id_cuenta_destino)
);