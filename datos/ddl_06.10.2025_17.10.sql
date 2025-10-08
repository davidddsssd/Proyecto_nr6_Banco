USE proyecto_banco;

CREATE TABLE IF NOT EXISTS direccion (
    id_direccion INT AUTO_INCREMENT,
    comuna VARCHAR(30) NOT NULL,
    calle VARCHAR(20) NOT NULL,
    departamento VARCHAR(20) NULL,
    numero_d VARCHAR(15) NOT NULL,

    CONSTRAINT pk_direccion PRIMARY KEY (id_direccion)
);

CREATE TABLE IF NOT EXISTS cliente (
    id_cliente INT AUTO_INCREMENT,
    id_direccion INT,
    nombre VARCHAR(30) NOT NULL,
    apellido VARCHAR(30) NOT NULL,
    rut VARCHAR(12) NOT NULL,
    telefono INT NOT NULL,
    mail VARCHAR(20) NULL,

    CONSTRAINT pk_cliente PRIMARY KEY (id_cliente),
    CONSTRAINT fk_direccion FOREIGN KEY (id_direccion) REFERENCES direccion(id_direccion)
);

CREATE TABLE IF NOT EXISTS cuenta (
    id_cliente INT,
    id_cuenta INT AUTO_INCREMENT,
    numero_c VARCHAR(15) NOT NULL,
    saldo FLOAT NOT NULL,
    fecha_apertura DATETIME NOT NULL,
    tipo_cuenta VARCHAR(15) NOT NULL,
    estado_cuenta BOOLEAN NOT NULL,

    CONSTRAINT pk_cuenta PRIMARY KEY (id_cuenta),
    CONSTRAINT fk_cliente FOREIGN KEY (id_cliente) REFERENCES cliente(id_cliente)
);

CREATE TABLE IF NOT EXISTS cuenta_destino (
    id_cuenta_destino INT AUTO_INCREMENT,
    tipo_cuenta_destino VARCHAR(15) NOT NULL,
    estado_cuenta_destino BOOLEAN NOT NULL,

    CONSTRAINT pk_cuenta_destino PRIMARY KEY (id_cuenta_destino)
);

CREATE TABLE IF NOT EXISTS transaccion (
    id_cuenta INT,
    id_transaccion INT AUTO_INCREMENT,
    id_cuenta_destino INT,
    tipo_transaccion VARCHAR(12) NOT NULL,
    fecha_transaccion DATETIME NOT NULL,
    monto FLOAT NOT NULL,

    CONSTRAINT pk_transaccion PRIMARY KEY (id_transaccion),
    CONSTRAINT fk_cuenta FOREIGN KEY (id_cuenta) REFERENCES cuenta(id_cuenta),
    CONSTRAINT fk_cuenta_destino FOREIGN KEY (id_cuenta_destino) REFERENCES cuenta_destino(id_cuenta_destino)
);