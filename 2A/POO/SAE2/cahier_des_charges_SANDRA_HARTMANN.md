# Projet SoftPhone Téléphonie IP

> Projet mis en place dans le cadre de la SAÉ 3.02
  Solution proposée par **SANDRA Valentin** et **HARTMANN Matthias**

## 1 - Cahier des charges

### Cahier des charges obligatoire du projet

- Création d'une application client/serveur basé sur un ou plusieurs protocols de transport (TCP/UDP)
- Utilisation d'un protocol applicatif, d'une base de donnée ou d'un système de fichier.
- Programmation en Python (*Ici en Python 3.9*)
- Application coté client unique pour tous les clients
- Création d'une interface graphique avec une option pour paramètres les éléments réseaux
- Utilisation du processus de sérialisation et désérialisation.

### Cahier des charges de la solution

- Un client doit pouvoir ouvrir le SoftPhone, s'enregistrer sur le serveur ou bien se connecter s'il est déjà enregistré
- Le client doit pouvoir avoir accès à la liste des clients connectés sur le serveur
- Le client doit pouvoir changer son mot de passe ou bien son nom/pseudo
- Le client ne doit pas pouvoir être en mesure d'obtenir l'adresse ip d'un autre client
- Le client doit pouvoir se déconnecter
- Le client doit recevoir des informations lorsqu'il est en appel. (temps d'appel, nom du correspondant...)
- Le client doit pouvoir créer un annuaire téléphonique lui permettant d'enregistrer le nom de certains clients afin de facilement les rappeler

- Le serveur doit pouvoir enregistrer les actions opérées (LOG)
- Le serveur doit pouvoir obtenir des informations sur un client
- Le serveur doit pouvoir être contrôlé à l'aide de commandes (Graphique ou Non)
- Le serveur doit pouvoir gérer plusieurs  clients en même temps (au moins 2)

### Améliorations éventuelles

> Dans le cas où les cahiers des charges précédents seraient implémentés et fonctionnels avant la livraison du projet, l'équipe pourrait mettre en place les améliorations suivantes

- Possibilité de faire sonner un client (appel non immédiat)
  - Interface permettant d'accepter ou non un appel entrant
  - Interface permettant de mettre en attente un appel et de décrocher un autre
- Mettre en place un système de statut d'apparence (Disponible, Absent, Occupé..)
- Mise en place de ConfCall (Appel avec plus de 2 interlocuteurs)
