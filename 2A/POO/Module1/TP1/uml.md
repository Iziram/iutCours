| Classe Article                                                            	|                                                                       	|
|---------------------------------------------------------------------------	|-----------------------------------------------------------------------	|
| **Attributs** :<br>- __nom: str<br>- __quantite: int<br>- __prix: float   	| Quantité sera automatiquement<br>mise à jour à chaque achat           	|
| **Méthodes :**<br>_\_init__(self, nom:str, quantite:int, prix:float)->None 	| initialisation des attributs                                          	|
| set(self, nom:str, quantite:int, prix:float)->None                        	| mise à jour des attributs                                             	|
| acheter(self, quantite)->float                                            	| pour acheter l'article (avec une certaine quantité)                   	|
| get(self)-> str                                                           	| retourne une représentation visuelle de l'article et de ses attributs 	|
| get_nom(self)->str                                                        	| retourne le nom de l'article                                          	|
| get_quantite(self)->int                                                   	| retourne la quantité de l'article                                     	|
| get_prix(self)->float                                                     	| retourne le prix unitaire de l'article                                	|
| get_attributs(self)->Tuple[str,int,float]                                 	| retourne les attributs dans un tuple                                  	|
| get_dict(self)->Dict[str,str or int or float]                             	| retourne l'article sous la forme d'un dictionnaire                    	|