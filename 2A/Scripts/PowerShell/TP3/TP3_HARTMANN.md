**BUT2 R&T - Module Script – Powershell - IUT Lannion**

**TP3 (2H) - Un script bien utile !**

Cet exercice introduit un cas pratique très fréquent pour les administrateurs système : la création automatique d’utilisateurs à partir d’un fichier CSV (Comma Separated Values). Ce TP se fera en mode 'projet'. Vous devez donc faire des recherches sur les commandes à utiliser.

<span style="color:red;">**Une restauration de Windows sera à faire 5 à 10mn avant la fin du TP.**</span>

# 1. Script de création de fichier CSV

Ci-après un exemple de contenu du fichier csv que vous aurez à traiter.
Vous vous y ajouterez en tant qu'enseignant et *vous ajouterez votre plus proche voisin en tant qu'étudiant de 2ème année*.

```csv
#Fichiers des utilisateurs à créer
nom, prenom, description, role, login
Dupont, Jean, étudiant de 1ère année, etudiant, jdupont
Lejeune, Clara, enseignante, enseignant, clejeune
Doisneau, Robert, étudiant de 2ème année, etudiant, rdoisneau 
```

* Créez un premier script **creationCSV.ps1**
* Créez une fonction **saisieInfos** demandant les informations suivantes à l'utilisateur :  `nom`, `prenom`, `description` et `rôle`.
  * la saisie du nom et du prenom doit avoir plus de 2 caractères
  * la description peut être vide
  * le rôle sera à choisir entre 'etudiant' ou 'enseignant'

* Créez une fonction **donneLogin** retournant le login à partir du nom et du prénom : première lettre du prénom suivie du nom.

* Dans un script principal : tant qu'il y a un utilisateur à créer, appeler les fonctions et ajouter les informations au fur et à mesure dans un même fichier CSV.

```powershell
function saisieInfos {
    $Title = "Saisie info"
    $Info = "Role de l'utilisateur"
    
    do {
        $nom = Read-Host -Prompt "Entrez le nom d'utilisateur  (minimum 2 caractères)"
    } while ($nom.Length -le 2)
    do {
        $prenom = Read-Host -Prompt "Entrez le prénom de l'utilisateur  (minimum 2 caractères)"
    } while ($prenom.Length -le 2)

    
    $description = Read-Host -Prompt "Entrez une description"

    $options = Write-Output etudiant enseignant
    $defaultchoice = 0
    $desc_selected = $host.UI.PromptForChoice($Title , $Info , $Options, $defaultchoice)

    return @{
        "nom"         = $nom
        "prenom"      = $prenom
        "description" = $description
        "role"        = $options[$desc_selected]
    }
}

function donneLogin($uti) {
    $login = $uti["prenom"].substring(0, 1) + $uti["nom"]
    return $login
}

if ( $(Test-Path -Path "./utilisateurs.csv") -eq $false ) {
    $texte = "nom, prenom, description, role, login"
    Out-File -FilePath "./utilisateurs.csv" -InputObject $texte
}

while ($(Read-Host -Prompt "Ajouter utilisateur ? (y/n)") -ne "n") {
    $util = saisieInfos
    $login = $(donneLogin $util)

    $line = "$($util.nom),$($util.prenom),$($util.description),$($util.role),$($login)"

    Add-Content "./utilisateurs.csv" $line
}
```

<span style="background-color:yellow;">**Valid 1 : Faire valider votre script de création de fichier CSV à l'enseignant**</span>

# 2. Script de création d'utilisateurs locaux

* Listez les utilisateurs locaux de votre machine dans votre CR.

  ```powershell
  Get-LocalUser
  ```

  ```console
  Name               Enabled Description
  ----               ------- -----------
  Administrateur     False   Compte d’utilisateur d’administration
  DefaultAccount     False   Compte utilisateur géré par le système.
  defaultuser100001  True
  Invité             False   Compte d’utilisateur invité
  Matthias           True
  Temp               True
  WDAGUtilityAccount False   Compte d’utilisateur géré et utilisé par le système pour les scénarios Windows Defender...
  ```

* Créez ensuite un script **creationUtilisateurLoc.ps1** qui prendra en paramètre le nom du fichier CSV à parcourir. Le script vérifiera que l'utilisateur n'existe pas déjà avant de le créer. Pour chaque utilisateur, vous devez créer son répertoire personnel dans C:\Users.

  ```powershell
  param (
    [string]$csvFile
  )
  if (-not (Test-Path $csvFile)) {
      Write-Host "Le fichier CSV spécifié n'existe pas."
      exit
  }

  $users = Import-Csv $csvFile

  foreach ($user in $users) {
      $username = $user.Login
      $exists = Get-LocalUser -Name $username -ErrorAction SilentlyContinue
      if ($exists) {
          Write-Host "L'utilisateur $username existe déjà."
      }
      else {
          $password = ConvertTo-SecureString "lannion" -AsPlainText -Force
          $nouveauUti = New-LocalUser -Name $username -Password $password -FullName "$($user.Prenom) $($user.Nom)" -Description $user.Description -ErrorAction SilentlyContinue
          if ($nouveauUti) {
              Write-Host "L'utilisateur $username a été créé avec succès."
              $userDir = "C:\Users\$username"
              New-Item -ItemType Directory -Path $userDir -ErrorAction SilentlyContinue
              Write-Host "Le répertoire personnel de l'utilisateur a été créé : $userDir"
          }
          else {
              Write-Host "Échec de la création de l'utilisateur $username."
          }
      }
  }

  ```

  ```console
  PS C:\WINDOWS\system32> C:\Users\Matthias\Desktop\IUT\iutCours\2A\Scripts\PowerShell\TP3\creationUtilisateurLoc.ps1 -csvFile C:\Users\Matthias\Desktop\IUT\iutCours\2A\Scripts\PowerShell\utilisateurs.csv

  L'utilisateur BRoss a été créé avec succès.

      Répertoire : C:\Users

  Mode                 LastWriteTime         Length Name
  ----                 -------------         ------ ----
  d-----        16/03/2023     09:03                BRoss
  Le répertoire personnel de l'utilisateur a été créé : C:\Users\BRoss
  L'utilisateur MBay a été créé avec succès.
  d-----        16/03/2023     09:03                MBay
  Le répertoire personnel de l'utilisateur a été créé : C:\Users\MBay

  PS C:\WINDOWS\system32> Get-LocalUser

  Name               Enabled Description
  ----               ------- -----------
  Administrateur     False   Compte d’utilisateur d’administration
  BRoss              True
  DefaultAccount     False   Compte utilisateur géré par le système.
  defaultuser100001  True
  Invité             False   Compte d’utilisateur invité
  Matthias           True
  MBay               True    bombe
  Temp               True
  WDAGUtilityAccount False   Compte d’utilisateur géré et utilisé par le système pour les scénarios Windows Defender Application Guard.

  PS C:\WINDOWS\system32> C:\Users\Matthias\Desktop\IUT\iutCours\2A\Scripts\PowerShell\TP3\creationUtilisateurLoc.ps1 -csvFile C:\Users\Matthias\Desktop\IUT\iutCours\2A\Scripts\PowerShell\utilisateurs.csv
  L'utilisateur BRoss existe déjÃ .
  L'utilisateur MBay existe déjÃ .

  ```

* Relistez les utilisateurs locaux de votre machine dans votre CR, ainsi que le répertoire C:\Users

  ```powershell
  Get-LocalUser
  Get-ChildItem -Path "C:\Users" | ForEach-Object { $_.PSChildName }

  ```

  ```txt
  PS C:\WINDOWS\system32> Get-LocalUser
  Get-ChildItem -Path "C:\Users" | ForEach-Object { $_.PSChildName }

  Name               Enabled Description                                                                                               
  ----               ------- -----------                                                                                               
  Administrateur     False   Compte d’utilisateur d’administration                                                                     
  BRoss              True                                                                                                              
  DefaultAccount     False   Compte utilisateur géré par le système.                                                                   
  defaultuser100001  True                                                                                                              
  Invité             False   Compte d’utilisateur invité                                                                               
  Matthias           True                                                                                                              
  MBay               True    bombe                                                                                                     
  Temp               True                                                                                                              
  WDAGUtilityAccount False   Compte d’utilisateur géré et utilisé par le système pour les scénarios Windows Defender Application Guard.
  
  
  BRoss
  Matthias
  MBay
  Public
  Temp
  ```
  
<span style="background-color:yellow;">**Valid 2 : Faire valider votre script de création d'utilisateur à l'enseignant**</span>

# 3. Création de dossiers partagés [bonus]

* Créez trois répertoires partagés pour vos utilisateurs :
  * `partage` accessible pour tous, en lecture et écriture,
  * `partageEns` accessible pour tous les enseignants, en lecture et écriture,
  * `consultation` accessible pour tous en lecture seulement.

```powershell

New-Item -ItemType Directory -Path "C:\partage"
New-Item -ItemType Directory -Path "C:\partageEns"
New-Item -ItemType Directory -Path "C:\consultation"

New-SmbShare -Name partage -Path "C:\partage" -FullAccess "Tout le monde"
New-SmbShare -Name partageEns -Path "C:\partageEns" -FullAccess "enseignant"
New-SmbShare -Name consultation -Path "C:\consultation" -ReadAccess "Tout le monde"

```

# 4. Script de suppression d’utilisateur

Proposez un script qui prend en paramètre un login et qui supprime l’utilisateur associé à ce login, s'il existe. Le script demandera s'il faut également supprimer le dossier personnel de l'utilisateur et si oui, alors tout le dossier personnel sera supprimé.

```powershell
  param (
      [string]$login
  )

  if (-not $login) {
      Write-Host "Veuillez fournir un login en paramètre."
      exit
  }

  $user = Get-LocalUser -Name $login -ErrorAction SilentlyContinue

  if ($user) {
      Remove-LocalUser -Name $login
      Write-Host "L'utilisateur $login a été supprimé avec succès."

      $supprimerDossier = Read-Host "Voulez-vous supprimer le dossier personnel de l'utilisateur ? (O/N)"

      if ($supprimerDossier -eq "O" -or $supprimerDossier -eq "o") {
          $userDir = "C:\Users\$login"
          if (Test-Path $userDir) {
              Remove-Item -Recurse -Force $userDir
              Write-Host "Le dossier personnel de l'utilisateur $login a été supprimé."
          }
          else {
              Write-Host "Le dossier personnel de l'utilisateur $login est introuvable."
          }
      }
  }
  else {
      Write-Host "L'utilisateur $login n'existe pas."
  }
```

```txt
PS C:\WINDOWS\system32> C:\Users\Matthias\Desktop\IUT\iutCours\2A\Scripts\PowerShell\supprimerUtilisateur.ps1 -login MBay
L'utilisateur MBay a été supprimé avec succès.
Voulez-vous supprimer le dossier personnel de l'utilisateur ? (O/N) : O
Le dossier personnel de l'utilisateur MBay a été supprimé.
```

<span style="background-color:yellow;">**Valid 3 : Faire valider la suppression d'un utilisateur à l'enseignant**</span>

<div style="page-break-after: always; visibility: hidden"> \pagebreak </div>

***

![Creative Commons](images/88x31.png)

[Ce document est mis à disposition selon les termes de la Licence Creative Commons Attribution - Pas d'Utilisation Commerciale - Pas de Modification 4.0 International](http://creativecommons.org/licenses/by-nc-nd/4.0/)

 IUT Lannion © 2023 by R&T is licensed under CC BY-NC-ND 4.0
