INSERT INTO direccion(id_direccion, comuna, calle, departamento, numero_d) VALUES
(1, 'Santiago Centro', 'Alameda', 'Depto 530B', '123'),
(2, 'Providencia', 'Nueva Providencia', 'Depto 504B', '456'),
(3, 'Ñuñoa', 'Irarrázaval', 'Depto 503C', '789'),
(4, 'Las Condes', 'El Bosque Norte', 'Depto 1202A', '321'),
(5, 'Maipú', 'Pajaritos', 'Depto 204B', '1001'),
(6, 'La Florida', 'Vicuña Mackenna', 'Depto 302', '1500'),
(7, 'Recoleta', 'Av. Recoleta', 'Depto 284A', '880'),
(8, 'Puente Alto', 'Concha y Toro', 'Depto 105', '2222'),
(9, 'Independencia', 'Gamero', 'Depto 354A', '300'),
(10, 'Estación Central', 'Coronel Souper', 'Depto 901', '111');

INSERT INTO cliente(id_cliente, id_direccion, nombre, apellido, rut, telefono, mail) VALUES
(),
();

INSERT INTO cuenta(id_cliente, id_cuenta, numero_c, saldo, fecha_apertura, tipo_cuenta, estado_cuenta) VALUES
(),
();

INSERT INTO cuenta_destino(id_cuenta_destino, tipo_cuenta_destino, estado_cuenta_destino) VALUES
(),
();

INSERT INTO transaccion(id_cuenta, id_transaccion, id_cuenta_destino, tipo_transaccion, fecha_transaccion, monto) VALUES
(),
();