SELECT * FROM empresa;
SELECT * FROM horario;
SELECT * FROM linea;
SELECT * FROM linea_parada;
SELECT * FROM paradas;
SELECT * FROM ruta;
SELECT * FROM viaje;

-- Cantidad de filas 
SELECT 'ruta' AS tabla, COUNT(*) FROM ruta
UNION ALL
SELECT 'viaje', COUNT(*) FROM viaje
UNION ALL
SELECT 'empresa', COUNT(*) FROM empresa;


--1. Consulta por clave primaria (ruta.id):
SELECT * FROM ruta WHERE id = 25;
EXPLAIN ANALYZE SELECT * FROM ruta WHERE id = 25;

--2. Búsqueda por destino en ruta:
SELECT
  r.origen,
  r.destino,
  v.hora_salida,
  v.hora_llegada
FROM ruta AS r
INNER JOIN viaje AS v
  ON v.ruta_id = r.id
WHERE r.destino = 'Mendoza Capital';


SELECT * FROM ruta WHERE destino = 'Mendoza Capital';
EXPLAIN ANALYZE SELECT * FROM ruta WHERE destino = 'Mendoza Capital';


CREATE INDEX idx_ruta_destino ON ruta(destino);
EXPLAIN ANALYZE SELECT * FROM ruta WHERE destino = 'Mendoza Capital';

--3. Consulta por costo base en un rango
SELECT * FROM viaje WHERE costo_base BETWEEN  1000 AND 2000;
EXPLAIN ANALYZE SELECT * FROM viaje WHERE costo_base BETWEEN 1000 AND 2000;

CREATE INDEX idx_viaje_costo_base ON viaje(costo_base);
EXPLAIN ANALYZE SELECT * FROM viaje WHERE costo_base BETWEEN 1000 AND 2000;

--4. índice compuesto en destino y costo base

SELECT v.costo_base FROM viaje v JOIN ruta r ON v.ruta_id = r.id WHERE r.destino = 'Mendoza Capital';
EXPLAIN ANALYZE SELECT v.costo_base FROM viaje v JOIN ruta r ON v.ruta_id = r.id WHERE r.destino = 'Mendoza Capital';

CREATE INDEX idx_viaje_ruta_costo ON viaje(ruta_id, costo_base);
EXPLAIN ANALYZE SELECT v.costo_base FROM viaje v JOIN ruta r ON v.ruta_id = r.id WHERE r.destino = 'Mendoza Capital';


--5. índice por empresa_id en viaje

SELECT * FROM viaje WHERE empresa_id = 3;
EXPLAIN ANALYZE SELECT * FROM viaje WHERE empresa_id = 3;

CREATE INDEX idx_viaje_empresa_id ON viaje(empresa_id);
EXPLAIN ANALYZE SELECT * FROM viaje WHERE empresa_id = 3;

DROP INDEX idx_viaje_empresa_id;

--6. Comparación entre índice B-tree y Hash en viaje.empresa_id

SELECT * FROM viaje WHERE empresa_id = 3;
EXPLAIN ANALYZE SELECT * FROM viaje WHERE empresa_id = 3;

--Indice b-tree
CREATE INDEX idx_viaje_empresa_btree ON viaje USING btree(empresa_id);
EXPLAIN ANALYZE SELECT * FROM viaje WHERE empresa_id = 3;

--Indice hash
DROP INDEX idx_viaje_empresa_btree;
CREATE INDEX idx_empresa_nombre_hash ON empresa USING hash(nombre);
EXPLAIN ANALYZE SELECT * FROM viaje WHERE empresa_id = 3;


