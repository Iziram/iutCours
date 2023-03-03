**BUT2 R&T - Module Script – Powershell - IUT Lannion**

**TP2 (3H) - Les fondamentaux**

> Utilisez l'aide afin de savoir comment utiliser les CMDlets spécifiques.

# 1. Exercice 1 : Redirection et pipeline

1. Redirigez la liste des commandes de Powershell dans un fichier texte **cmdLets.txt** en utilisant la
commande ``Out-File``

```powershell
Get-Command -CommandType Cmdlet | Out-File "cmdLets.txt"
```

2. Avec une seule commande, redirigez dans un fichier **extensions.txt** toutes les extensions *différentes*
des fichiers contenus dans un répertoire donné. Attention, on ne veut pas de doublons !

Exemple de résultat :

```console
> cat .\extensions.txt
.1
.8
.android
.cfg
.eclipse
.jmc
.packettracer
.thumbnails
.txt
.virtualbox
.vscode
```

```powershell
Get-ChildItem -Path . -File | Select-Object Extension -Unique | ForEach-Object {$_.Extension}
```

**Résultat**

```txt
PS C:\Users\Matthias\Desktop\IUT\iutCours\2A\Scripts> Get-ChildItem -Path . -File | Select-Object Extension -Unique | ForEach-Object {$_.Extension}
```

# 2. Exercice 2 : Filtre Where-Object

1. Donnez la liste des fichiers dont la taille excède 500 octets.

  ```powershell
  Get-ChildItem | Where-Object { $_.Length -gt 500 } | Select-Object Name, Length

  ```

  **Résultat**

  ```txt
  
  PS C:\Users\Matthias\Desktop\IUT\iutCours\2A\Scripts> Get-ChildItem | Where-Object { $_.Length -gt 500 } | Select-Object Name, Length   

  Name  Length
  ----  ------
  cmdLets.txt 430080
  test.txt  125772
  ```

2. Listez les services stoppés.

  ```powershell
  Get-Service | Where-Object { $_.Status -eq "Stopped" } | Select-Object Name
  ```

  **Résultat**

  ```txt
  PS C:\Users\Matthias\Desktop\IUT\iutCours\2A\Scripts>   Get-Service | Where-Object { $_.Status -eq "Stopped" } | Select-Object Name
  Name
  ----
  AarSvc_16e71e9
  AJRouter
  ALG
  AppIDSvc
  AppReadiness
  autotimesvc
  AxInstSV
  BcastDVRUserService_16e71e9
  BDESVC
  BITS
  BluetoothUserService_16e71e9
  Browser
  BTAGService
  bthserv
  CaptureService_16e71e9
  CertPropSvc
  ClipSVC
  COMSysApp
  ConsentUxUserSvc_16e71e9
  CredentialEnrollmentManagerUserSvc_16e71e9
  dcsvc
  defragsvc
  DeviceAssociationBrokerSvc_16e71e9
  DeviceInstall
  DevicePickerUserSvc_16e71e9
  DevicesFlowUserSvc_16e71e9
  DevQueryBroker
  diagnosticshub.standardcollector.service
  diagsvc
  DmEnrollmentSvc
  dmwappushservice
  DoSvc
  dot3svc
  DsmSvc
  DsSvc
  Eaphost
  EasyAntiCheat_EOS
  edgeupdate
  edgeupdatem
  ```

3. Listez les processus dont le temps d'occupation processeur est supérieur à 300 millisecondes.

  ```powershell
  Get-Process | Where-Object { $_.TotalProcessorTime -gt 300 } | Select-Object Name, TotalProcessorTime
  ```

  **Résultat**

  ```txt
  
    PS C:\Users\Matthias\Desktop\IUT\iutCours\2A\Scripts>   Get-Process | Where-Object { $_.TotalProcessorTime -gt 300 } | Select-Object Name, TotalProcessorTime

    Name                        TotalProcessorTime
    ----                        ------------------
    ApplicationFrameHost        00:00:00.1250000  
    AsusOptimizationStartupTask 00:00:00.0625000  
    AsusOSD                     00:00:00.0468750  
    AsusSoftwareManagerAgent    00:00:00.2031250 

  ```

**Validation : Faites valider vos 3 dernières lignes de commandes à l'enseignant encadrant**

<div style="page-break-after: always; visibility: hidden"> \pagebreak </div>

# 3. Exercice 3 : Les boucles

1. Dans un script, déclarez un tableau de 100 cases initialisées de 0 à 99. Puis à l'aide d'une boucle `while`, afficher sur la sortie standard toutes les cases du tableau.

```powershell
# Déclaration du tableau de 100 cases
$tableau = 0..99

# Initialisation de la variable d'itération
$i = 0

# Boucle while pour afficher les cases du tableau
while ($i -lt $tableau.Length) {
    Write-Output $tableau[$i]
    $i++
}

```

**Résultat**

```txt
PS C:\Users\Matthias\Desktop\IUT\iutCours\2A\Scripts> . 'C:\Users\Matthias\Desktop\IUT\iutCours\2A\Scripts\PowerShell\TP2\script.ps1'     
0
1
2
3
4
5
6
7
8
9
10
...
```

2. Dans un script, demandez, à un utilisateur de saisir un nombre compris entre 0 et 10. Puis intégrez cette demande dans une boucle `do...while` afin que la demande soit réitérée si la saisie n'est pas correcte.

3. Affichez de nouveau le tableau de la question 1 mais cette fois avec une boucle `for`.
4. Affichez tous les processus sous la forme suivante à l'aide de la boucle `foreach` :

```console
unsecapp démarré le : 03/23/2020 15:22:28
Video.UI démarré le : 03/23/2020 15:20:54
wininit démarré le :
winlogon démarré le :
```

5. `Foreach-object` permet une segmentation entre les tâches à effectuer avant le premier objet, les tâches à effectuer pour chaque objet, et les tâches à effectuer après le dernier objet. En une seule ligne de commande, donnez la liste des processus sous la forme suivante :

```console
Liste des processus
ApplicationFrameHost
BackupManagerTray
BrcmCardReader
. . .
Fin de la liste des processus
```

<div style="page-break-after: always; visibility: hidden"> \pagebreak </div>

# 4. Exercice 4 : Structure conditionnelle

1. Après avoir demandé 2 variables entières à l'utilisateur, indiquez si la première est plus grande ou égale à la seconde ou si elle est plus petite :

```console
Nombre 1 : 15
Nombre 2 : 6
15 est plus grand ou égal à 6
```

2. Avec une suite de if/elseif, indiquez si un nombre saisi par l'utilisateur est 1, 2, 3 ou si c'est un autre nombre :

```console
Votre nombre : 3
la valeur saisie est égale à 3
Votre nombre : 6
la valeur n'est pas égale à 1, ni à 2, ni à 3
```

3. Même exercice mais avec la commande switch et en allant jusque 5 :

```console
Votre nombre : 6
la valeur saisie n'est pas comprise entre 1 et 5
Votre nombre : 3
la valeur saisie est égale à 3
```

<div style="page-break-after: always; visibility: hidden"> \pagebreak </div>

# 5. Exercice 5 : les fonctions

1. Entraînez vous à créer des fonctions.
Par exemple, créer une fonction Bonjour qui affichera "Bonjour, nous sommes le samedi 4 mars 2023", en utilisant la date du système, bien sûr !
2. Fonction avec arguments : dans un script, reprennez l'exercice 4.3 dans une fonction et appelez ensuite cette fonction en passant l'entier en argument :

```console
function maFct {
. . .
}
maFct 2
maFct 3
maFct 10
```

donnera :

```console
la valeur saisie est égale à 2
la valeur saisie est égale à 3
la valeur saisie n'est pas comprise entre 1 et 5
```

3. Créez une fonction moyenne (en précisant le nom des paramètres) qui retourne la moyenne de 2 nombres. L'appel de la fonction devra préciser le nom des paramètres.

* Exemple d'appel de la fonction : `moyenne -nb1 15 -nb2 20`
* Exemple de résultat : `La moyenne de 15 et 20 est de 17.5`

**Validation : Faites valider votre fonction `moyenne` à l'enseignant encadrant**

# 6. Exercice 6 : Génération de nombre « aléatoires » dans testFonction.ps1

* Dans un script nommé `testFonction.ps1` définissez une fonction nommée nbAlea qui utilise une instance de l’objet system.random pour retourner un nombre aléatoire. Le programme principal sera composé d’une boucle `for` effectuant 10 appels à la fonction `nbAlea` et qui affiche le nombre retourné.
* Définissez ensuite une autre fonction qui teste si un nombre est pair ou impair.
* Testez votre fonction dans votre boucle.
* Modifiez votre programme pour que la fonction `nbAlea` accepte un paramètre correspondant au nombre de nombres aléatoires à générer. L’itération s’effectuera donc dans la fonction `nbAlea`.

**Validation : Faites valider votre script `testFonction.ps1` à l'enseignant encadrant**

<div style="page-break-after: always; visibility: hidden"> \pagebreak </div>

# 7. Exercice 7 :. Interactions avec l’utilisateur dans testInteraction.ps1

Dans un script nommé `testInteraction.ps1`, vous allez définir une fonction nommée `saisieEmail` dont le rôle est de demander à l’utilisateur de saisir son adresse mail et de vérifier que celle-ci est d’un format valide.

La fonction retournera l’adresse mail saisie. Vous utiliserez une boucle de type `do … while` pour continuer à demander une adresse mail tant que celle saisie n’est pas valide.

Le test de validité se fera à l’aide de l’opérateur like dont un exemple d’utilisation est donné ci-dessous.

```console
PS C:\Users\Sophie> $var = "test.ps1"
PS C:\Users\Sophie> if ($var -like '*.ps1') { Write-Host "C'est un script
Powershell ";} else { Write-Host "C'est pas du powershell";}
C'est un script Powershell
```

**Validation : Faites valider votre script `testInteraction.ps1` à l'enseignant encadrant**

<div style="page-break-after: always; visibility: hidden"> \pagebreak </div>

# 8. Exercice 8 : Un script complet

1. Proposez un script `liste.ps1` prenant en paramètre un nom de dossier et affichant son contenu.
2. Pour chaque élément affiché vous devez indiquer s’il s'agit d'un dossier ou d'un fichier.

Vous utiliserez la `cmd-let Get-ChildItem` et la propriété `PsIsContainer` pour savoir si l'élément manipulé est un dossier ou un fichier.

Exemple d’exécution de votre script :

```console
PS C:\Users\Sophie> .\liste.ps1 "C:\Users\Sophie\IUT\2A Scripts"
TP1 - Affichage des fichiers et répertoires de 'C:\Users\Sophie\IUT\2A Scripts' :
Répertoire : 2020
Répertoire : Docs
Fichier : ex.doc
Fichier : ExCours39.ps1
Fichier : ExCours46.ps1
```

3. Complétez le script précédant pour que le paramètre du nom de dossier soit nommé dir et que le script accepte un second paramètre nommé filtre permettant de demander l’affichage des fichiers ou des dossiers.

Voici un exemple d’invocation de votre script `liste.ps1`

```console
.\liste.ps1 –dir C:\ -filtre fichier
.\litse.ps1 –dir C:\ -filtre dossier
```

**Validation : Faites valider votre script `liste.ps1` à l'enseignant encadrant**

# 9. Exercice 9 : Un peu de style

Colorer sa console... Powershell vous permet d'agir sur la console à travers l'objet `host.ui.RawUI`

* Listez les propriétés de cet objet.
* Changez la couleur de fond de votre fenêtre ainsi que la couleur de votre texte.

<div style="page-break-after: always; visibility: hidden"> \pagebreak </div>

***

![Creative Commons](images/88x31.png)

[Ce document est mis à disposition selon les termes de la Licence Creative Commons Attribution - Pas d'Utilisation Commerciale - Pas de Modification 4.0 International](http://creativecommons.org/licenses/by-nc-nd/4.0/)

 IUT Lannion © 2023 by R&T is licensed under CC BY-NC-ND 4.0
