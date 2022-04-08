-- ----------------------------------------------------------------------------
-- BDR : Introduction aux Bases de Données Relationnelles
-- compteRenduTP2.sql
-- Nom Prénom : HARTMANN Matthias
-- ----------------------------------------------------------------------------
--
-- ----------------------------------------------------------------------------
-- TP2 - interrogation de données (requêtes SELECT sur plusieurs tables)
-- base "Confiserie"
-- ----------------------------------------------------------------------------
--
-- ----------------------------------------------------------------------------
--A) Découverte des différentes tables de la base
-- ----------------------------------------------------------------------------
-- 1- Listez les tables de la base ainsi que leur structure (schéma en intention de la base) :
	/*
	pg_mhartmann=> \d
             Liste des relations
 Schéma |     Nom      | Type  | Propriétaire 
--------+--------------+-------+--------------
 public | acheter      | table | mhartmann
 public | boulangeries | table | mhartmann
 public | friandises   | table | mhartmann
 public | gourmands    | table | mhartmann
 public | vendre       | table | mhartmann



	*/
-- 2- Donnez les requêtes qui vous permettent de lister le contenu des 5 tables de la base (schéma en extension de la base): 
	/*
	select * from <table>;
	*/
-- 3- Contenu des tables :
--	ACHETER :
/*
 nog | nof | nob 
-----+-----+-----
 G1  | F1  | B1
 G1  | F1  | B2
 G1  | F1  | B3
 G1  | F1  | B6
 G1  | F3  | B1
 G1  | F3  | B4
 G1  | F4  | B5
 G1  | F6  | B1
 G1  | F6  | B2
 G1  | F6  | B6
 G1  | F10 | B2
 G1  | F10 | B4
 G1  | F13 | B2
 G2  | F1  | B3
 G2  | F1  | B6
 G2  | F8  | B6
 G3  | F6  | B2
 G3  | F6  | B4
 G3  | F7  | B4
 G3  | F10 | B2
 G3  | F11 | B2
 G3  | F13 | B2
 G4  | F2  | B2
 G4  | F3  | B1
 G4  | F4  | B2
 G4  | F6  | B1
 G4  | F6  | B2
 G4  | F6  | B6
 G4  | F13 | B2
 G5  | F4  | B5
 G5  | F7  | B5


boulangeries :
 nob |          nom           
-----+------------------------
 B1  | La Mie Câline
 B2  | La Fournée de Ker Huel
 B3  | Au Fournil Gourmand
 B4  | Boulangerie Fagnou
 B5  | La Flûte Dorée
 B6  | Au Fournil d'Emile
 B7  | Super U

Friandises
 nof |       nom       
-----+-----------------
 F1  | Fraise Tagada
 F2  | Dragibus
 F3  | Mentos
 F4  | Fruikipik
 F5  | Michoko
 F6  | Fimousse
 F7  | Chupa-Chups
 F8  | Chamallow
 F9  | Malabar
 F10 | Regal'ad
 F11 | Pâtes de fruits
 F12 | Acidofilo
 F13 | Tropifrutti

gourmands
 nog |  nom   
-----+--------
 G1  | Tom
 G2  | Léa
 G3  | Tof
 G4  | Enzo
 G5  | Sarah
 G6  | Nathan

vendre
 nob | nof 
-----+-----
 B1  | F1
 B1  | F3
 B1  | F6
 B1  | F10
 B2  | F1
 B2  | F2
 B2  | F4
 B2  | F6
 B2  | F10
 B2  | F11
 B2  | F13
 B3  | F1
 B4  | F3
 B4  | F6
 B4  | F7
 B4  | F8
 B4  | F10
 B5  | F4
 B5  | F7
 B5  | F8
 B5  | F12
 B6  | F1
 B6  | F6
 B6  | F8

*/
--
-- ----------------------------------------------------------------------------
--B) Interrogation de la BD-R "Confiserie" 
-- ----------------------------------------------------------------------------
-- Donnez les requêtes SQL correspondant aux questions suivantes (cf. étude faite en TD), exécutez-les, notez le résultat et commentez si besoin :
-- 1- Quels sont les numéros des boulangeries (classés en ordre croissant) chez lesquelles le gourmand G1 se ravitaille ?
select distinct(nob) 
from acheter 
where nog = 'G1' 
order by nob asc;
-- 2- Quels sont les noms des gourmands et le numéro des boulangeries dont ils sont clients ?
select distinct gourmands.nom,nob 
from acheter 
INNER JOIN gourmands on acheter.nog = gourmands.nog 
order by gourmands.nom asc;
-- 3- Combien de friandises sont vendues par chacune des boulangeries (les boulangeries seront classées par ordre alphabétique inverse) ?
select nom, count(*) as nombre 
from vendre 
INNER JOIN boulangeries on vendre.nob = boulangeries.nob 
GROUP BY nom
order by nom DESC;

-- 4- Quels sont les numéros des boulangeries où Léa se ravitaille ? 
select distinct nob 
from acheter 
where nog = (select nog from gourmands where nom='Léa');
-- 5- Quels sont les numéros des friandises que Nathan achète ? 
select distinct nof 
from acheter 
where nog = (select nog from gourmands where nom='Nathan');
-- 6- Quels sont les noms des boulangeries chez lesquelles Sarah ou Léa se ravitaillent ? 
select distinct nom from acheter INNER JOIN boulangeries on boulangeries.nob = acheter.noB where nog in (select nog from gourmands where nom in ('Léa','Sarah'));

-- 7- Quels sont les noms des boulangeries chez lesquelles plus de 2 enfants se ravitaillent ? 
select nom from (select distinct nob,nog from acheter) as R 
INNER JOIN boulangeries on R.nob = boulangeries.nob 
GROUP BY nom 
HAVING count(*) > 2; 
-- 8- Quels sont les noms des gourmands et les noms des boulangeries dont ils sont clients ?
select distinct gourmands.nom, boulangeries.nom 
from acheter 
INNER JOIN boulangeries on acheter.nob = boulangeries.noB 
INNER JOIN gourmands on acheter.nog = gourmands.nog; 
-- 9- Quels sont les noms des boulangeries et les noms des friandises qu'elles vendent ?
select distinct boulangeries.nom, friandises.nom
from vendre 
INNER JOIN boulangeries on vendre.nob = boulangeries.noB 
INNER JOIN friandises on vendre.nof = friandises.nof; 
-- 10- Quels sont les noms des boulangeries chez lesquelles Enzo se ravitaille ?
select distinct boulangeries.nom 
from acheter 
INNER JOIN boulangeries on acheter.nob = boulangeries.noB 
where acheter.nog = (select nog from gourmands where nom = 'Enzo');
-- 11- Quels sont les numéros des boulangeries qui vendent des friandises que Léa achète ?
select distinct nob 
from vendre
where nof in 
(select distinct nof from acheter where nog = (select nog from gourmands where nom = 'Léa'));

-- 12- Quels sont les noms des boulangeries chez lesquelles Enzo et Sarah (à la fois) se ravitaillent ? 
select nom from boulangeries where nob in (select nob
from (select nob from acheter where nog = (select nog from gourmands where nom = 'Enzo')) as t
INTERSECT (select nob from acheter where nog = (select nog from gourmands where nom = 'Sarah'))) 
;
-- 13- Quels sont les noms des boulangeries chez lesquelles Léa ne se fournit pas ?
select nom 
from boulangeries 
where nob not in (select nob from acheter where nog = (select nog from gourmands where nom = 'Léa'));

-- 14- Quels sont les noms des boulangeries qui vendent des friandises que Léa achète ?
select nom 
from boulangeries
where nob in 
(select nob from vendre where nof in (select distinct nof 
from acheter 
where nog = (select nog from gourmands where nom='Léa')))
;

-- 15- Quels sont les noms des gourmands qui se ravitaillent dans toutes les boulangeries ?
select nom from (select distinct nog, nob from acheter) as r INNER JOIN gourmands on r.nog = gourmands.nog GROUP BY nom having count(*) = (select count(*) from boulangeries);
-- 16- Quels sont les noms des gourmands qui n’achètent pas de friandise ? 
select nom from gourmands where nog not in (select distinct nog from acheter);

insert into acheter VALUES
('G7','F1','B1'),
('G7','F1','B2'),
('G7','F1','B3'),
('G7','F3','B4'),
('G7','F4','B5'),
('G7','F1','B6'),
('G7','F1','B7');
