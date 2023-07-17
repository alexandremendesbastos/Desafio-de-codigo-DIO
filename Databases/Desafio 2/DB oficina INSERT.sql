USE Oficina;

SELECT * FROM PessoaFisica;
INSERT INTO PessoaFisica VALUES 
    (1, 'João', 12345678910, 'Rua A, 123', '11137564556'),
    (2, 'Maria', 08975386541, 'Rua B, 456', '11997665745'),
    (3, 'José', 78531297453, 'Rua C, 789', '11091184726'),
    (4, 'Ana', 89674435241, 'Rua D, 987', '11997674632'),
    (5, 'Pedro', 90877865576, 'Rua E, 654', '11976556477'),
    (6, 'Mariana', 07795647385, 'Rua F, 321', '11999098896');

SELECT * FROM Veiculo;
INSERT INTO Veiculo VALUES 
    (1, 1, 'ABC1234'),
    (2, 2, 'DEF5678'),
    (3, 3, 'GHI9012'),
    (4, 4, 'JKL3456'),
    (5, 5, 'MNO7890'),
    (6, 6, 'PQR2345');

SELECT * FROM Conserto;
INSERT INTO Conserto VALUES 
    (1, 'Problemas no motor'),
    (2, 'Troca de óleo'),
    (3, 'Freios desgastados'),
    (4, 'Bateria descarregada'),
    (5, 'Problemas na suspensão'),
    (6, 'Troca de pneus');

SELECT * FROM Mecanico;
INSERT INTO Mecanico VALUES 
    (1, 'Carlos', 'Rua X, 789', 'Motor'),
    (2, 'Fernanda', 'Rua Y, 456', 'Elétrica'),
    (3, 'Renato', 'Rua Z, 123', 'Freios'),
    (4, 'Laura', 'Rua W, 987', 'Bateria'),
    (5, 'Marcos', 'Rua V, 654', 'Suspensão'),
    (6, 'Carolina', 'Rua U, 321', 'Pneus');

SELECT * FROM OdServiço;
INSERT INTO OdServiço VALUES 
    (1, '2023/07/01', '150.00', '25.00', '175.00', 'AGUARDANDO', NULL),
    (2, '2023/07/02', '200.00', '50.00', '250.00', 'CONCLUIDO', '2023/07/03'),
    (3, '2023/07/03', '300.00', '75.00', '375.00', 'CONCLUIDO', '2023/07/04'),
    (4, '2023/07/04', '250.00', '30.00', '280.00', 'EM ANDAMENTO', NULL),
    (5, '2023/07/05', '400.00', '80.00', '480.00', 'CANCELADO', NULL),
    (6, '2023/07/06', '350.00', '40.00', '390.00', 'EM ANDAMENTO', NULL);

SELECT * FROM Autorização;
INSERT INTO Autorização VALUES 
    (1, FALSE),
    (2, TRUE),
    (3, TRUE),
    (4, TRUE),
    (5, FALSE),
    (6, TRUE);

SELECT * FROM Pecas;
INSERT INTO Pecas VALUES 
    (1, 'Vela de ignição', '15.00'),
    (2, 'Filtro de óleo', '10.00'),
    (3, 'Pastilha de freio', '50.00'),
    (4, 'Bateria', '150.00'),
    (5, 'Amortecedor', '100.00'),
    (6, 'Pneu', '80.00');

SELECT * FROM Serviços;
INSERT INTO Serviços VALUES 
    (1, 'Troca de correia dentada', '120.00'),
    (2, 'Troca de óleo e filtro', '50.00'),
    (3, 'Revisão completa', '300.00'),
    (4, 'Troca de bateria', '100.00'),
    (5, 'Alinhamento e balanceamento', '80.00'),
    (6, 'Troca de pneus', '200.00');

SELECT Autorização.Autorizado, OdServiço.idOdServiço, Clientes.idClientes
    FROM Autorização
    CROSS JOIN OdServiço, Clientes;
