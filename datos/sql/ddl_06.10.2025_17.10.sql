USE proyecto_banco;

CREATE TABLE IF NOT EXISTS direcciones (
    id_direccion INT AUTO_INCREMENT,
    comuna VARCHAR(50) NOT NULL,
    calle VARCHAR(50) NOT NULL,
    departamento VARCHAR(20) NULL,
    numero_d VARCHAR(15) NOT NULL,

    CONSTRAINT pk_direccion PRIMARY KEY (id_direccion)
);

CREATE TABLE IF NOT EXISTS clientes (
    id_cliente INT AUTO_INCREMENT,
    id_direccion INT,
    nombre VARCHAR(30) NOT NULL,
    apellido VARCHAR(30) NOT NULL,
    rut VARCHAR(12) NOT NULL UNIQUE,
    telefono VARCHAR(15) NOT NULL UNIQUE,
    mail VARCHAR(50) NULL,

    CONSTRAINT pk_cliente PRIMARY KEY (id_cliente),
    CONSTRAINT fk_direccion FOREIGN KEY (id_direccion) REFERENCES direcciones(id_direccion)
);

CREATE TABLE IF NOT EXISTS cuentas (
    id_cuenta INT AUTO_INCREMENT,
    id_cliente INT,
    numero_c VARCHAR(20) NOT NULL UNIQUE,
    saldo INT NOT NULL,
    fecha_apertura DATETIME NOT NULL,
    tipo_cuenta ENUM('corriente', 'ahorro', 'vista') NOT NULL,
    estado_cuenta BOOLEAN NOT NULL,

    CONSTRAINT pk_cuenta PRIMARY KEY (id_cuenta),
    CONSTRAINT fk_cliente FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente)
);

CREATE TABLE IF NOT EXISTS cuentas_destino (
    id_cuenta_destino INT AUTO_INCREMENT,
    tipo_cuenta_destino VARCHAR(15) NOT NULL,
    estado_cuenta_destino BOOLEAN NOT NULL,
    nombre_titular VARCHAR(60) NULL,

    CONSTRAINT pk_cuenta_destino PRIMARY KEY (id_cuenta_destino)
);

CREATE TABLE IF NOT EXISTS transacciones (
    id_transaccion INT AUTO_INCREMENT,
    id_cuenta INT,
    id_cuenta_destino INT,
    tipo_transaccion VARCHAR(12) NOT NULL,
    fecha_transaccion DATETIME NOT NULL,
    monto INT NOT NULL,
    descripcion VARCHAR(100) NULL,
    
    CONSTRAINT pk_transaccion PRIMARY KEY (id_transaccion),
    CONSTRAINT fk_cuenta FOREIGN KEY (id_cuenta) REFERENCES cuentas(id_cuenta),
    CONSTRAINT fk_cuenta_destino FOREIGN KEY (id_cuenta_destino) REFERENCES cuentas_destino(id_cuenta_destino)
);