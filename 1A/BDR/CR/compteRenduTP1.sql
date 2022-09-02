-- ----------------------------------------------------------------------------
-- BDR : Introduction aux Bases de Données Relationnelles
-- compteRenduTP1.sql
-- Nom Prénom :
-- ----------------------------------------------------------------------------
--
-- ----------------------------------------------------------------------------
-- TP1 - Prise en main de postegreSQL et psql
--       + interrogation de données (requêtes SELECT sur une table)
-- base "AnnoncesAuto"
-- ----------------------------------------------------------------------------
--
-- ----------------------------------------------------------------------------
-- EXERCICE 1 - Prise en main de l'interpréteur de commande SQL psql
-- ----------------------------------------------------------------------------
--
--1.A) Préliminaires
-- Récupération des fichiers nécessaires à cette séance de TP
-- Déplacement dans le répertoire où est copié le script de commandes AnnoncesAuto.sql 
-- Connexion à la base sur le SGBD postgreSQL (commande à finaliser) : 
      psql -h 148.60.237.2 -p 5433 -U <login> -d pg_<login>
-- Création d'un alias pour la connexion au SGBD (commande à finaliser) : 
      echo alias cnx_PG="'psql -h 148.60.237.2 -p 5433 -U <login> -d pg_<login>'"  >> /home/eturt/<login>/.bash_aliases
-- Vérification de l'alias
--
--1.B) Mise en œuvre du client psql
-- Testez les commandes psql pour :
-- 1. afficher l'aide sur les commandes de psql :
	-- \n
-- 2. lister les commandes SQL ou afficher l’aide sur la syntaxe d’une commande SQL (e.g. SELECT) :
	-- \h
-- 3. connaître la liste des bases disponibles :
	-- \l
-- 4. connaître la liste des tables disponibles dans votre base :
	-- \d
-- 5. exécuter le script de commandes SQL AnnoncesAuto.sql :
	-- \ir AnnonceAuto.sql
--   (ensuite, listez à nouveau le contenu de votre base)
-- 6. connaître le schéma en intention de la table annonces :
	-- \d annonces
-- 7. connaître les utilisateurs :
	-- \dg
-- requête SQL pour obtenir le nombre de tuples de la table annonces :
	select count(*) from annonces;
-- requête SQL pour obtenir le schéma en extension de la table annonces :
	select * from annonces;
-- 8. supprimer l'affichage du nom des attributs (réactiver l'affichage avec la même commande) :
	-- \t
-- 9. afficher les valeurs des tuples en colonne (revenir à l'affichage en ligne par la même commande):
	-- \x
-- Tester ces mises en forme sur la requête suivante : 
   SELECT * FROM annonces WHERE annee = 1995 ;
--
--1.C) Bonus
-- 10. Complétez la table annonces avec les données mémorisées dans "ajoutAnnonces.csv" :
   \copy annonces from ajoutAnnoncesPG.csv with csv header
-- Requête SQL qui permet de vérifier que la table annonces contient maintenant 6 tuples concernant des véhicules datant de 1995 :
-- 11. Sauvegardez le résultat de cette requête SQL au format csv avec en-tête dans le fichier "selection1.csv"  :
   \copy (select * from annonces where annee = 1995) to selection1.csv with csv header
--
-- Avant d’interroger votre base (cf. Exercice 2), rétablissez l’état d’origine de votre table annonces :
-- supprimer tous les tuples de la table :
-- remplir la table avec les 1000 tuples mémorisés dans le fichier "annoncesPG.csv" :
-- vérifier que la table contient bien 1000 tuples dont 3 concernant des véhicules datant de 1995 :
--
-- ----------------------------------------------------------------------------
-- EXERCICE 2 - Interrogation de la base avec psql (clause SELECT)
-- ----------------------------------------------------------------------------
--
-- Donnez les requêtes SQL correspondant aux demandes suivantes, exécutez-les, 
-- notez le résultat (s'il n'est pas trop volumineux ou sinon, seulement les premiers tuples) et commentez :
-- 1)Affichez toutes les informations sur toutes les annonces (1000 tuples).
	Select * from annonces;
/*	idannonce |   marque   |                                    designation                                    | annee | kilometrage | nvxoption | nvxconfort | nvxsecurite | cylindree | puissance | prix  | consommation 
-----------+------------+-----------------------------------------------------------------------------------+-------+-------------+-----------+------------+-------------+-----------+-----------+-------+--------------
    302539 | renault    | VelSatis 2.2 DCI GPS 3D 2006 Carminat                                             |  2006 |      171000 |         2 |          2 |           1 |       2.2 |       140 |  7300 |          9.0
*/
-- 2)Affichez toutes les informations des annonces qui concernent des voitures de marque Audi (204 tuples).
	select * from annonces where marque = 'audi';
	/*
	idannonce | marque |                               designation                                | annee | kilometrage | nvxoption | nvxconfort | nvxsecurite | cylindree | puissance | prix  | consommation 
-----------+--------+--------------------------------------------------------------------------+-------+-------------+-----------+------------+-------------+-----------+-----------+-------+--------------
    302757 | audi   | PEUGEOT 406 Coupé - 2.2L 16V Pack
	*/
-- 3)Affichez la designation, l'année et le prix des voitures dont le kilométrage est inférieur à 20000 (73 tuples).
	select designation, annee, prix from annonces where kilometrage < 20000;
	/*
	                     designation                      | annee | prix  
------------------------------------------------------+-------+-------
 VOLKSWAGEN PASSAT 2.0 TDI 140ch CONFORTLINE          |  2009 | 19490
 Peugeot 407 Coupé 2.0L HDI 136cv Féline 9800Kms      |  2008 | 26500
 307 cc super occaz peu km                            |  2005 | 19500
 Subaru impreza WRX                                   |  2008 |      
 Seat toledo style 2.0 tdi 140 cv                     |  2009 | 19793
 Seat toledo style 2.0 tdi 140 cv                     |  2009 | 19793
 AUDI A5 Cabriolet S-LINE 2.0 TSI 211 Quattro         |  2009 | 46900

	*/
-- 4)En utilisant deux syntaxes différentes, affichez la designation et le prix des voitures dont le prix est compris entre 4000 et 10000 (non strictement) et dont la consommation est inférieure ou égale à 7 (33 tuples).
	select designation, prix from annonces where prix between 4000 and 10000;
	select designation, prix from annonces where prix >= 4000 and prix <= 10000;
	/*
	                            designation                            | prix  
-------------------------------------------------------------------+-------
 VelSatis 2.2 DCI GPS 3D 2006 Carminat                             |  7300
 Renault laguna 1.9 dci 120 cv initiale 2001                       |  6700
 Peugeot 307 2.0 l hdi 110 cv serie xt clim 5 ptes                 |  6700
 Altea 2.0 tdi 140cv                                               |  9500
 Peugeot 407 -2.0 hdi -136 CV                                      |  8900
 VelSatis 2.2 DCI GPS 3D 2006 Carminat                             |  7300

	*/
-- 5)En utilisant deux syntaxes différentes, affichez la désignation, le prix et le kilométrage des voitures dont la marque est soit renault, soit peugeot, soit citroen (436 tuples). 
	select designation, prix , kilometrage from annonces where marque in ('renault','peugeot','citroen');
	select designation, prix , kilometrage from annonces where marque = 'renault' or marque = 'peugeot' or marque = 'citroen';
	/*
	                              designation                               | prix  | kilometrage 
------------------------------------------------------------------------+-------+-------------
 VelSatis 2.2 DCI GPS 3D 2006 Carminat                                  |  7300 |      171000
 Renault laguna 1.9 dci 120 cv initiale 2001                            |  6700 |      194000
 Peugeot 307 2.0 l hdi 110 cv serie xt clim 5 ptes                      |  6700 |      128642
 Peugeot 407 -2.0 hdi -136 CV                                           |  8900 |      155000

	*/
-- 6)Affichez toutes les informations des voitures dont le niveau de sécurité est supérieur à 2 et dont le niveau d'option ou le niveau de confort est supérieur à 5 (36 tuples).
	select * from annonces where nvxsecurite > 2 and (nvxoption > 5 or nvxconfort > 5); 
	/*
	idannonce |   marque   |                                designation                                 | annee | kilometrage | nvxoption | nvxconfort | nvxsecurite | cylindree | puissance | prix  | consommation 
-----------+------------+----------------------------------------------------------------------------+-------+-------------+-----------+------------+-------------+-----------+-----------+-------+--------------
    302835 | audi       | Audi a4 new ambition 2.0 tdi fap                                           |  2009 |       24000 |        10 |          4 |           3 |       2.0 |       143 | 26300 |          9.0

	*/
-- 7)Affichez la designation, le prix et le kilométrage des voitures dont la désignation contient le mot clé 'tdi' (252 tuples).
	select designation, prix, kilometrage from annonces where designation like '%tdi%';
	/*
	                     designation                      | prix  | kilometrage 
------------------------------------------------------+-------+-------------
 Altea 2.0 tdi 140cv                                  |  9500 |      123500
 Audi a4 new ambition 2.0 tdi fap                     | 26300 |       24000

	*/
-- 8)Affichez dans une colonne nommée prixMin le prix le plus bas (1 tuple).
	select min(prix) as prixMin from annonces;
	/*
	 prixmin 
---------
    1000

	*/
-- 9)Affichez toutes les informations sur la voiture la moins chère en utilisant la valeur numérique obtenue dans la requête précédente (1 tuple). 
--   Puis, obtenez ce même affichage sans utiliser la valeur numérique de la requête précédente mais une requête imbriquée.
	select * from annonces where prix = 1000;
	select * from annonces where prix = (select min(prix) as prixMin from annonces);
	/*
	idannonce | marque |        designation        | annee | kilometrage | nvxoption | nvxconfort | nvxsecurite | cylindree | puissance | prix | consommation 
-----------+--------+---------------------------+-------+-------------+-----------+------------+-------------+-----------+-----------+------+--------------
    276810 | audi   | Audi A4 1.9 TDI accidenté |  1996 |      190000 |         1 |          2 |           1 |       1.9 |        90 | 1000 |          9.0
(1 ligne)
*/
-- 10)L'instruction LIMIT X (existante dans plusieurs SGBD dont postgreSQL) permet de ne retourner que les X premiers tuples de la relation résultat. Par exemple, 
      SELECT * FROM annonces WHERE  annee = 1995 LIMIT 5; 
--    ne retournera que les 5 premières annonces répondant à la condition de sélection. 
--    En utilisant cette instruction LIMIT ainsi qu'une instruction de classement des tuples, proposez une nouvelle requête répondant à la question 9.
	select * from annonces order by prix ASC limit 1;
	/*
	idannonce | marque |        designation        | annee | kilometrage | nvxoption | nvxconfort | nvxsecurite | cylindree | puissance | prix | consommation 
-----------+--------+---------------------------+-------+-------------+-----------+------------+-------------+-----------+-----------+------+--------------
    276810 | audi   | Audi A4 1.9 TDI accidenté |  1996 |      190000 |         1 |          2 |           1 |       1.9 |        90 | 1000 |          9.0
(1 ligne)
*/
-- 11)Affichez dans une colonne nommée prixMoyAudi le prix moyen des voitures de marque Audi (1 tuple).
	select avg(prix) as prixMoyAudi where marque ='audi';
	/*
	    prixmoyaudi     
--------------------
 15642.134328358209
(1 ligne)
*/
--
-- Déconnexion de la base :
	-- \q
--

