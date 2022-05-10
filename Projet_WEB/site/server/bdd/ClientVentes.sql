
CREATE TABLE IF NOT EXISTS Produits (
 idP INTEGER PRIMARY KEY AUTOINCREMENT,
 NomP VARCHAR (20),
 Prix INTEGER
 );

CREATE TABLE IF NOT EXISTS Acheteurs (
 idC INTEGER PRIMARY KEY AUTOINCREMENT,
 NomP VARCHAR (20),
 Ville VARCHAR (20)
 );

CREATE TABLE IF NOT EXISTS Achat (
 idP INTEGER ,
 idC INTEGER ,
 Qte INTEGER,
 PRIMARY KEY (idP, idC),
 CONSTRAINT fk_idP FOREIGN KEY (idP) REFERENCES Produits(idP) ON DELETE CASCADE ON UPDATE CASCADE,
 CONSTRAINT fk_idC FOREIGN KEY (idC) REFERENCES Acheteurs(idC) ON DELETE CASCADE ON UPDATE CASCADE 
 );


INSERT INTO Produits (idP, NomP,  Prix) VALUES(1 ,'Tondeuse' , 250);
INSERT INTO Produits (idP, NomP,  Prix) VALUES(2 ,'Trotinette'  , 50);
INSERT INTO Produits (idP, NomP,  Prix) VALUES(3 ,'Table'  , 10);
INSERT INTO Produits (idP, NomP,  Prix) VALUES(4 ,'Vélo'  , 1000);

INSERT INTO  Acheteurs (idC, NomP, Ville) VALUES (1 ,'Thomas' ,'Bordeaux');
INSERT INTO Acheteurs (idC, NomP, Ville) VALUES(2 ,'Alice' ,'Morlaix' );
INSERT INTO Acheteurs (idC, NomP, Ville) VALUES(3 ,'Margot' ,'Paris' );
INSERT INTO Acheteurs (idC, NomP, Ville)VALUES (4 ,'Lola' ,'Lannion' );

INSERT INTO Achat (idP,idC,Qte) VALUES (1, 1, 1);
INSERT INTO Achat (idP,idC,Qte) VALUES (1, 2, 1);
INSERT INTO Achat (idP,idC,Qte) VALUES (2, 1, 1);
INSERT INTO Achat (idP,idC,Qte) VALUES (3, 3, 30);
INSERT INTO Achat (idP,idC,Qte) VALUES (3, 2, 50);
INSERT INTO Achat (idP,idC,Qte) VALUES (1, 4, 20);
INSERT INTO Achat (idP,idC,Qte) VALUES (4, 1, 18);
INSERT INTO Achat (idP,idC,Qte) VALUES (4, 4, 50);
INSERT INTO Achat (idP,idC,Qte) VALUES (1, 3, 5);
INSERT INTO Achat (idP,idC,Qte) VALUES (4, 3, 6);
