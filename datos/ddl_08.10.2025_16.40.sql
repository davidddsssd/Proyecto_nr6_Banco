INSERT INTO direccion(id_direccion, comuna, calle, departamento, numero_d) VALUES
(),
();

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