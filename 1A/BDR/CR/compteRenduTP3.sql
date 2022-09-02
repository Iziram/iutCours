-- ----------------------------------------------------------------------------
-- BDR : Introduction aux Bases de Données Relationnelles
-- compteRenduTP3.sql
-- Nom Prénom :
-- ----------------------------------------------------------------------------
--
-- ----------------------------------------------------------------------------
-- TP3 - Définition, manipulation et interrogation de données 
--        (requêtes ALTER - UPDATE, INSERT - SELECT)
-- base "Confiserie"
-- ----------------------------------------------------------------------------
--
-- ----------------------------------------------------------------------------
-- EXERCICE 1- Ajouts d'attributs (Alter TABLE)
-- ----------------------------------------------------------------------------
-- Donnez les requêtes permettant de faire les modifications suivantes et vérifiez leur effet sur la base :
-- 1.	Ajoutez une nouvelle colonne PRIX (de type réel,toujours positive) à la table VENDRE. 
alter table vendre add prix float;
alter table vendre add constraint vendre_prix_ck CHECK(vendre.prix >= 0);
-- 2.	Ajoutez une nouvelle colonne VILLE à votre table GOURMANDS.
alter table gourmands add ville varchar(100);
--
-- ----------------------------------------------------------------------------
-- EXERCICE 2-  Modifications et ajouts de N-uplets (UPDATE, INSERT INTO)
-- ----------------------------------------------------------------------------
-- Donnez les requêtes permettant de faire les modifications suivantes et relevez leur résultat :
-- 1.	Le nom d’une des friandises est incorrect. Corrigez cette erreur en remplaçant "Fimousse" par "Pimousse".
update friandises set nom='Pimousse' where nom='Fimousse';

-- 2.	Les requêtes 5/ et 12/ du TP2 donnent des relations vides (sans tuple).	
--      Afin d’avoir au moins un tuple résultat à chacune de ces 2 requêtes, entrez dans la base les informations suivantes :
--          Nathan achète des Mentos à la Boulangerie Fagnou :
insert into acheter (nog,nob,nof) 
(
select * from (select nog from gourmands where nom='Nathan') as I 
CROSS JOIN (select nob from boulangeries where nom='Boulangerie Fagnou') as S
CROSS JOIN (select nof from friandises where nom='Mentos') as T
);

insert into acheter (nog,nob,nof) 
VALUES
(
(select nog from gourmands where nom='Nathan'),
(select nob from boulangeries where nom='Boulangerie Fagnou'),
(select nof from friandises where nom='Mentos')
);
--          Enzo n’achète pas des Fruikipik à la Fournée de Ker Huel mais à la Flûte Dorée (boulangerie fréquentée par Sarah) :
update acheter set nob=
(select nob from boulangeries 
where nom='La Flûte Dorée'
)
where nob=
(select nob from boulangeries 
where nom='La Fournée de Ker Huel'
) 
and nog=
(select nog from gourmands 
where nom='Enzo'
)
and nof=
(select nof from friandises 
where nom='Fruikipik'
) ;
--          Sarah n’achète pas des Chupa-Chups à la Flûte dorée mais des Mentos à la Mie Câline :
update acheter
set nob=(select nob from boulangeries where nom='La Mie Câline'),
nof=(select nof from friandises where nom='Mentos')
where 
nob=(select nob from boulangeries where nom = 'La Flûte Dorée')
and 
nof=(select nof from friandises where nom='Chupa-Chups')
and
nog=(select nog from gourmands where nom='Sarah');


--
-- 3.	Mettez à jour les prix des différentes confiseries, 
--		en fixant d’abord le prix de base de chacune :
--			Fraise Tagada  : 0.25 €			Dragibus : 0.7 € 		Mentos : 0.52 €			Fruikipik : 1 €		Michoko : 0.81 €
--			Pimousse : 0.1 €				Chupa-Chups : 0.5 €		Chamallow : 0.75 €		Malabar : 1.1 €		Regal'ad : 0.6 €	
--			Pâtes de fruits : 0.8 €			Acidofilo  et  Tropifrutti : 0.55 €

update vendre set prix=0.25 where nof=(select nof from friandises where nom = 'Fraise Tagada');
update vendre set prix=0.1 where nof=(select nof from friandises where nom = 'Pimousse');
update vendre set prix=0.8 where nof=(select nof from friandises where nom = 'Pâtes de fruits');
update vendre set prix=0.7 where nof=(select nof from friandises where nom = 'Dragibus');
update vendre set prix=0.5 where nof=(select nof from friandises where nom = 'Chupa-Chups');
update vendre set prix=0.55 where nof in (select nof from friandises where nom = 'Acidofilo' or nom='Tropifrutti');
update vendre set prix=0.52 where nof=(select nof from friandises where nom = 'Mentos');
update vendre set prix=0.75 where nof=(select nof from friandises where nom = 'Chamallow');
update vendre set prix=1 where nof=(select nof from friandises where nom = 'Fruikipik');
update vendre set prix=1.1 where nof=(select nof from friandises where nom = 'Malabar');
update vendre set prix=0.81 where nof=(select nof from friandises where nom = 'Michoko');
update vendre set prix=0.6 where nof=(select nof from friandises where nom = 'Regal''ad');

--		puis en appliquant le coefficient pratiqué par chacune des boulangeries sur ces prix de base : 
--			La Mie Câline et Au Fournil Gourmand pratiquent les prix de base --> coeff. = 1
--			La Flûte Dorée --> 0.8 		La Fournée de Ker Huel --> 0.9 		Boulangerie Fagnou --> 1.1
--			Au Fournil d’Emile --> 1.2		(Super U --> 1.3)
update vendre set prix=prix*0.8 where nob=(select nob from boulangeries where nom='La Flûte Dorée');
update vendre set prix=prix*0.9 where nob=(select nob from boulangeries where nom='La Fournée de Ker Huel');
update vendre set prix=prix*1.2 where nob=(select nob from boulangeries where nom='Au Fournil d''Emile');
update vendre set prix=prix*1.1 where nob=(select nob from boulangeries where nom='Boulangerie Fagnou');
--
-- 4.	Mettez à jour la colonne VILLE de la table GOURMANDS sachant que 
--  	Tom, Tof et Sarah habitent à Lannion tandis que Léa et Nathan résident à Perros-Guirec et Enzo à Trégastel. 
update gourmands set ville='Lannion' where nom in ('Tom','Tof','Sarah');
update gourmands set ville='Perros-Guirec' where nom in ('Léa','Nathan');
update gourmands set ville='Trégastel' where nom in ('Enzo');
-- ----------------------------------------------------------------------------
-- EXERCICE 3- Interrogation de la base
-- ----------------------------------------------------------------------------
-- Donnez les requêtes permettant de répondre aux questions suivantes, exécutez-les et relevez leur résultat :
-- 1.	Quels sont les différents prix des "Fraise Tagada" ? 
select distinct prix from vendre where nof=(select nof from friandises where nom = 'Fraise Tagada');
/*
 prix  
-------
 0.225
  0.25
   0.3
*/
-- 2.	Quel est le prix moyen des confiseries de chacune des boulangeries ? 
select nom,avg(prix) from vendre INNER JOIN boulangeries on vendre.noB = boulangeries.noB group by nom ;
/*
          nom           |        avg        
------------------------+-------------------
 La Mie Câline          |            0.3675
 Boulangerie Fagnou     |            0.5434
 Au Fournil d'Emile     |              0.44
 La Flûte Dorée         |              0.56
 La Fournée de Ker Huel | 0.514285714285714
 Au Fournil Gourmand    |              0.25

*/
-- 3.	Quel est le prix moyen des confiseries de chacune des boulangeries ordonnés du meilleur marché au plus cher ? 
select nom,avg(prix) from vendre INNER JOIN boulangeries on vendre.noB = boulangeries.noB group by nom ORDER BY avg(prix) ASC;
/*
          nom           |        avg        
------------------------+-------------------
 Au Fournil Gourmand    |              0.25
 La Mie Câline          |            0.3675
 Au Fournil d'Emile     |              0.44
 La Fournée de Ker Huel | 0.514285714285714
 Boulangerie Fagnou     |            0.5434
 La Flûte Dorée         |              0.56

*/
-- 4.	Quel est le prix moyen des confiseries de "La Mie Câline" ? 
select nom,avg(prix) from vendre INNER JOIN boulangeries on vendre.noB = boulangeries.noB group by nom HAVING nom='La Mie Câline';
/*
      nom      |  avg   
---------------+--------
 La Mie Câline | 0.3675

*/
-- 5.	Où demeure Enzo ? 
select ville from gourmands where nom = 'Enzo';
/*
   ville   
-----------
 Trégastel

*/
-- 6.	Où habitent les gourmands achetant des confiseries "Au Fournil d'Emile" ?
select nom, ville from gourmands where nog in 
(select nog from acheter where nob = 
(select nob from boulangeries where nom = 'Au Fournil d''Emile')
);
/*
   nom    |     ville     
----------+---------------
 Tom      | Lannion
 Léa      | Perros-Guirec
 Enzo     | Trégastel

*/
-- 7.	Quels sont les Lannionais achetant des "Fraise Tagada" ?
select nom from gourmands where nog in 
(select nog from acheter where nof = 
(select nof from friandises where nom ='Fraise Tagada')
)
and
ville = 'Lannion';
/*
 nom 
-----
 Tom
*/
-- 8.	Reprenez les requêtes du TP2 auxquelles vous n’avez pas répondu. 
