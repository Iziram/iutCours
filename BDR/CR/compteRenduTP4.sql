-- ----------------------------------------------------------------------------
-- BDR : Introduction aux Bases de Données Relationnelles
-- compteRenduTP4.sql
-- Nom Prénom : Hartmann Matthias
-- ----------------------------------------------------------------------------
--
-- ----------------------------------------------------------------------------
-- TP4 - Définition, manipulation et interrogation de données 
--       (requêtes CREATE, ALTER - UPDATE, INSERT, DELETE - SELECT)
-- base "Confiserie"
-- ----------------------------------------------------------------------------
--
-- ----------------------------------------------------------------------------
-- EXERCICE 1- Création de table (CREATE TABLE) et ajout d'attribut (ALTER TABLE)
-- ----------------------------------------------------------------------------
-- 1-A) Préliminaire
-- 		1.	Exécutez le script de commandes ConfiserieTP4.sql.
-- 		2.	Vérifiez que votre base contient les 2 nouvelles tables R1 et CONFISEURS 
--		3.	Relevez les extensions de ces 2 tables et vérifiez-les
--R1
/*
          nomb          |       nomd        |          webd           | codepostald |            villed             
------------------------+-------------------+-------------------------+-------------+-------------------------------
 La Mie Câline          | HUETTE            | www.huette.fr           |       56950 | Crach
 La Mie Câline          | TIPIAK            | www.tipiak.fr           |       29170 | Fouesnant
 La Fournée de Ker Huel | BRIDOR            | www.bridordefrance.com  |       35538 | Servon sur Vilaine
 Au Fournil Gourmand    | BELLOT MINOTERIES | www.bellotminoteries.fr |       79400 | Saint-Martin-De-Saint-Maixent
 Boulangerie Fagnou     | BELLOT MINOTERIES | www.bellotminoteries.fr |       79400 | Saint-Martin-De-Saint-Maixent
 Boulangerie Fagnou     | BRIDOR            | www.bridordefrance.com  |       35538 | Servon sur Vilaine
 Boulangerie Fagnou     | TIPIAK            | www.tipiak.fr           |       29170 | Fouesnant
 La Flûte Dorée         | BELLOT MINOTERIES | www.bellotminoteries.fr |       79400 | Saint-Martin-De-Saint-Maixent
 Au Fournil d'Emile     | BRIDOR            | www.bridordefrance.com  |       35538 | Servon sur Vilaine
 Super U                | EURODISTRIBUTION  | www.eurodistribution.fr |       69003 | Lyon

*/
/*
Confiseur
 noc |        nom         |    pays    
-----+--------------------+------------
   1 | Haribo             | Allemagne
   2 | Perfetti Van Melle | Etats-Unis
   3 | La Pie Qui Chante  | France
   4 | Kréma              | France

*/
--
-- 1-B) Création des tables DISTRIBUTEURS et FOURNIR
-- 		1.	Donnez les commandes SQL permettant de créer ces deux tables dont les schémas sont les suivants :
--          DISTRIBUTEURS :  { PK (noD entier), nom varchar(20), URLweb varchar(30), code entier, ville varchar(50) }

create table distributeurs(
noD serial primary key,
nom varchar(20) not null,
URLWeb varchar(30),
code integer default 0,
ville varchar(50)

constraint distributeurs_code_ck check(code >= 0),
constraint distributeurs_urlweb_ck check( URLWeb like 'www.%.%')
);

create table fournir(
noB varchar(3) ,
noD integer,

constraint fournir_pk primary key (noB, noD),
constraint fournir_noB_fk foreign key (noB) references boulangeries (noB)
	on UPDATE CASCADE,
constraint fournir_noD_fk foreign key (noD) references distributeurs (noD)
	on UPDATE CASCADE on DELETE CASCADE

);
--			FOURNIR :        { PK (# noB varchar(3), # noD entier) }
--          avec les contraintes données dans le sujet					
-- 		2.	Exécutez vos commandes et vérifiez la bonne création des tables DISTRIBUTEURS et FOURNIR.
--
-- 1-C) Ajoutez à la table FRIANDISES un attribut noC de type entier qui fait référence au (numéro de) confiseur fabriquant la friandise,
--      avec les contraintes données dans le sujet.
alter table friandises add  noC integer ;
alter table friandises add constraint friandises_noC_fk 
foreign key (noC) references confiseurs (noC) on UPDATE cascade on delete set null;

--
-- ---------------------------------------------------------------------------------------
-- EXERCICE 2-  Peuplement de tables à partir d’une relation unique (INSERT INTO + SELECT)
--              + Complétion des données (UPDATE)
-- ---------------------------------------------------------------------------------------
select nomd, webd,codepostald,villed from r1;
insert into distributeurs (nom,urlweb,code,ville) (select nomd, webd,codepostald,villed from r1);

select noB, noD from r1 inner join boulangeries on boulangeries.nom = r1.nomB inner join distributeurs on distributeurs.nom = r1.nomD;
insert into fournir (noB,noD) (select noB, noD from r1 inner join boulangeries on boulangeries.nom = r1.nomB inner join distributeurs on distributeurs.nom = r1.nomD);
-- 2-A) Peuplement des tables DISTRIBUTEURS et FOURNIR à partir notamment des informations contenues dans la table R1.
--      et vérification
--
-- 2-B) Complétion avec les valeurs de l’attribut friandises.noC sachant que :
--      Chupa-Chups et Mentos sont produits par Perfetti Van Melle
update friandises set 
noC=(select noc from confiseurs where nom ='Perfetti Van Melle') 
where friandises.nom in ('Chupa-Chups','Mentos');
--      Fraise Tagada, Dragibus, Fruikipik, Chamallow, Acidofilo et Tropifrutti sont produits par  Haribo
update friandises set 
noC=(select noc from confiseurs where nom ='Haribo') 
where friandises.nom in ('Fraise Tagada', 'Dragibus', 'Fruikipik', 'Chamallow', 'Acidofilo','Tropifrutti');
--      Michoko et Pimousse sont produits par La Pie Qui Chante
update friandises set 
noC=(select noc from confiseurs where nom ='La Pie Qui Chante') 
where friandises.nom in ('Michoko','Pimousse');
--      Malabar et Regal'ad sont produits par Kréma
update friandises set 
noC=(select noc from confiseurs where nom ='Kréma') 
where friandises.nom in ('Malabar','Regal''ad');
--      Pâtes de fruits n'a pas de producteur 
update friandises set 
noC=null
where friandises.nom in ('Pâtes de fruits');
--		
-- ----------------------------------------------------------------------------
-- EXERCICE 3- Interrogation de la base (SELECT) 
-- ----------------------------------------------------------------------------
-- Donnez les requêtes permettant de répondre aux questions suivantes, exécutez-les et relevez leur résultat :
-- 1.	Quels sont les noms des distributeurs mémorisés dans la base 
select distinct(nom) from distributeurs;
-- 2.	Quel est le nom du confiseur produisant chaque friandise ?
select friandises.nom, confiseurs.nom from friandises inner join confiseurs on friandises.noc = confiseurs.noc;
-- 3.	Quelles sont les villes des gourmands qui vont dans les boulangeries se ravitaillant chez BRIDOR.
select distinct(noB) from fournir where noD in 
(select noD from distributeurs where nom ='BRIDOR');
select distinct(ville) from gourmands inner join acheter on acheter.noG = gourmands.noG inner join 
(select distinct(noB) from fournir where noD in 
(select noD from distributeurs where nom ='BRIDOR')) as R on r.noB = acheter.nob;
-- 4.	Donnez les noms des distributeurs et le nombre de boulangeries qu’ils ravitaillent. 
select nom,count(*) from fournir inner join distributeurs on distributeurs.noD = fournir.noD group by nom;
-- 5.	Quels sont les noms des Lannionais consommateurs de confiseries de La Pie Qui Chante ?
select noF from friandises where noC = (select noc from confiseurs where nom = 'La Pie Qui Chante');

select distinct(nom) from gourmands 
inner join acheter on acheter.noG = gourmands.noG 
where 
noF in (select noF from friandises where noC = (select noc from confiseurs where nom = 'La Pie Qui Chante'))
and ville ='Lannion';

-- ----------------------------------------------------------------------------
-- EXERCICE 4- Modification des données (UPDATE, DELETE FROM) 
-- ----------------------------------------------------------------------------
-- Donnez les requêtes permettant de réaliser les modifications suivantes, exécutez-les, relevez et commentez leur effet sur l’ensemble de la base :
-- 1.	Supprimez le distributeur "Bellot Minoteries".
delete from distributeurs where nom = 'BELLOT MINOTERIES';
/*
Les tuples ayant le noD du distributeur ont été supprimées de la base
*/
-- 2.	Supprimez le confiseur "Kréma".
delete from confiseurs where nom = 'Kréma';
/*
Les tuples ayant la clé étrangère noC ont remplacé la clé étrangère par NULL

*/
-- 3.	Ajoutez 100 à tous les numéros de distributeur dans la table DISTRIBUTEURS
update distributeurs set noD = noD+100;
/*
Les tuples ayant la clé étrangère noD ont été mis à jour avec la nouvelle valeur de chaque noD
*/
-- 4.	Multipliez par 100 tous les numéros de confiseur dans la table CONFISEURS.
update confiseurs set noc = noc*100;
/*
Les clés étrangère noC ont été mise à jours.
*/
