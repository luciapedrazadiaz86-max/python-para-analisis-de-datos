INSERT INTO Cliente VALUES
(101, 'Federación de Grandes Empresas', 'Av. Constituyentes 123, Querétaro', 'ONG'),
(102, 'Comercio Digital SA', 'Calle Madero 27, Querétaro', 'Comercio'),
(103, 'Autopartes del Bajío SA', 'Av. 5 de Febrero 20, Querétaro', 'Automotriz'),
(104, 'Banco Banko', 'Av. Zaragoza 12, Querétaro', 'Banca'),
(105, 'Mudanzas Rápidas SA', 'Calle Hidalgo 138, Querétaro', 'Logística');

INSERT INTO Curso VALUES
(12, 'Inglés para logística', 'Inglés', 'A1', 10, '2020-02-01', 1, 1, 105),
(13, 'Inglés básico', 'Inglés', 'A2', 40, '2019-11-12', 0, 6, 101),
(14, 'Inglés intermedio', 'Inglés', 'B2', 40, '2019-11-12', 0, 6, 101),
(15, 'Inglés avanzado', 'Inglés', 'C1', 40, '2019-11-12', 0, 6, 101),
(16, 'Mandarín para la industria automotriz', 'Mandarín', 'B1', 15, '2020-01-15', 1, 3, 103),
(17, 'Francés intermedio', 'Francés', 'B1', 18, '2020-04-03', 0, 2, 101),
(18, 'Alemán para principiantes', 'Alemán', 'A2', 8, '2020-02-14', 1, 4, 102),
(19, 'Inglés intermedio', 'Inglés', 'B2', 10, '2020-03-29', 0, 1, 104),
(20, 'Ruso avanzado', 'Ruso', 'C1', 4, '2020-04-08', 0, 5, 103);

INSERT INTO Participante VALUES
(101, 'Marina', 'Bermúdez', '4421558182', 101),
(102, 'Andrea', 'Durán', '4421555740', 101),
(103, 'Felipe', 'Prado', '4421555692', 102),
(104, 'René', 'Bravo', '4421555546', 102),
(105, 'Susana', 'Suárez', '4421555779', 102),
(106, 'Cristian', 'Serrano', '4421555375', 101),
(107, 'Enrique', 'Quintero', '4421555633', 101),
(108, 'Juan', 'Navarro', '4421555824', 101),
(109, 'Pablo', 'García', '4421555176', 101),
(110, 'Melina', 'Delgado', '4421555527', 103),
(111, 'Diego', 'Durán', '4421555311', 103),
(112, 'Maximiliano', 'Morales', '4421555195', 104),
(113, 'Ximena', 'Morales', '4421555355', 104),
(114, 'Héctor', 'Flores', '4421555581', 105);

INSERT INTO Tomar_curso VALUES
(101, 15), (101, 17), (102, 17), (103, 18), (104, 18), (105, 18),
(106, 13), (107, 13), (108, 13), (109, 14), (109, 15), (110, 16),
(110, 20), (111, 16), (114, 12), (112, 19), (113, 19);