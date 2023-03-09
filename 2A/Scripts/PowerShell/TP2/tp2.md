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

    **Résultat:**

    ```txt
    PS C:\Users\Matthias\Desktop\IUT\iutCours\2A\Scripts> Get-ChildItem -Path . -File | Select-Object Extension -Unique | ForEach-Object {$_.Extension}
    ```

# 2. Exercice 2 : Filtre Where-Object

1. Donnez la liste des fichiers dont la taille excède 500 octets.

    ```powershell
    Get-ChildItem | Where-Object { $_.Length -gt 500 } | Select-Object Name, Length

    ```

    **Résultat:**

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

    **Résultat:**

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

  **Résultat:**

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
    $tableau = 0..99
    $i = 0
    while ($i -lt $tableau.Length) {
        Write-Output $tableau[$i]
        $i++
    }

    ```

    **Résultat:**

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

    **Script :**

    ```powershell
    $nombre = -1
    do {
        [int]$nombre = Read-Host "Entrez un nombre entre 0 et 10 : "
    } while (($nombre -lt 0 ) -or ($nombre -gt 10) )

    Write-Output "Vous avez saisi le nombre : $nombre"
    ```

    **Résultat:**

    ```txt
    PS F:\iutCours\2A> . 'F:\iutCours\2A\Scripts\PowerShell\TP2\script.ps1'
    Entrez un nombre entre 0 et 10 : : -1
    Entrez un nombre entre 0 et 10 : : 11
    Entrez un nombre entre 0 et 10 : : 12
    Entrez un nombre entre 0 et 10 : : 23
    Entrez un nombre entre 0 et 10 : : 1
    Vous avez saisi le nombre : 1
    ```

3. Affichez de nouveau le tableau de la question 1 mais cette fois avec une boucle `for`.

    **Script:**

    ```powershell
    $tableau = 0..99
    for ($i = 0; $i -lt $tableau.Length; $i++) {
        Write-Output $tableau[$i]
    }

    ```

    **Résultat:**

    ```txt
    PS F:\iutCours\2A> . 'F:\iutCours\2A\Scripts\PowerShell\TP2\script.ps1'
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

4. Affichez tous les processus sous la forme suivante à l'aide de la boucle `foreach` :

    ```console
    unsecapp démarré le : 03/23/2020 15:22:28
    Video.UI démarré le : 03/23/2020 15:20:54
    wininit démarré le :
    winlogon démarré le :
    ```

    **Script:**

    ```powershell
    $processes = Get-Process
    foreach ($process in $processes) {
        if ($null -ne $process.StartTime) {
            $startTime = $process.StartTime.ToString('yyyy-MM-dd HH:mm:ss')
            Write-Host "Processus : $($process.Name) démarré le : $startTime"
        }
    }

    ```

    **Résultat:**

    ```txt
    F:\iutCours\2A> . 'F:\iutCours\2A\Scripts\PowerShell\TP2\script.ps1'
    amdow démarré le : 2023-03-08 20:27:16
    AMDRSServ démarré le : 2023-03-08 20:27:15
    AMDRSSrcExt démarré le : 2023-03-08 20:32:16
    ApCent démarré le : 2023-03-08 20:26:53
    ApplicationFrameHost démarré le : 2023-03-08 20:27:38
    audiodg démarré le : 2023-03-02 16:12:20
    CalculatorApp démarré le : 2023-03-08 20:27:38
    ...
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

    **Script:**

    ```powershell
    "Liste des processus$(Get-Process | ForEach-Object { "`n"+$_.Name })`nFin des processus"
    ```

    **Résultat:**

    ```txt
    PS F:\iutCours\2A> "Liste des processus$(Get-Process | ForEach-Object { "`n"+$_.Name })`nFin des processus"
    Liste des processus
    AdjustService
    amdfendrsr
    amdow
    AMDRSServ
    AMDRSSrcExt
    ```

<div style="page-break-after: always; visibility: hidden"> \pagebreak </div>

# 4. Exercice 4 : Structure conditionnelle

1. Après avoir demandé 2 variables entières à l'utilisateur, indiquez si la première est plus grande ou égale à la seconde ou si elle est plus petite :

    ```console
    Nombre 1 : 15
    Nombre 2 : 6
    15 est plus grand ou égal à 6
    ```

    **Script:**

    ```powershell
    [int]$NB1 = Read-Host "Nombre 1"
    [int]$NB2 = Read-Host "Nombre 2"
    if ($NB1 -ge $NB2) {
        Write-Host "$NB1 est plus grand ou égal à $NB2."
    }
    else {
        Write-Host "$NB1 est plus petit que $NB2"
    }
    ```

    **Résultat:**

    ```txt
    F:\iutCours\2A> . 'F:\iutCours\2A\Scripts\PowerShell\TP2\script.ps1'
    Nombre 1 : 15
    Nombre 2 : 6
    15 est plus grand ou égal à 6.

    F:\iutCours\2A> . 'F:\iutCours\2A\Scripts\PowerShell\TP2\script.ps1'
    Nombre 1 : 6
    Nombre 2 : 15
    6 est plus petit que 15
    ```

2. Avec une suite de if/elseif, indiquez si un nombre saisi par l'utilisateur est 1, 2, 3 ou si c'est un autre nombre :

    ```console
    Votre nombre : 3
    la valeur saisie est égale à 3
    Votre nombre : 6
    la valeur n'est pas égale à 1, ni à 2, ni à 3
    ```

    **Script:**

    ```powershell
    [int]$nb = Read-Host "Votre nombre"

    if($nb -eq 1){
        Write-Host "La valeur saisie est égale à 1"
    }
    elseif($nb -eq 2){
        Write-Host "La valeur saisie est égale à 2"
    }
    elseif($nb -eq 3){
        Write-Host "La valeur saisie est égale à 3"
    }
    else{
        Write-Host "la valeur n'est pas égale à 1, ni à 2, ni à 3"

    }
    ```

    **Résultat:**

    ```txt
    F:\iutCours\2A> . 'F:\iutCours\2A\Scripts\PowerShell\TP2\script.ps1'
    Votre nombre : 3
    La valeur saisie est égale à 3

    F:\iutCours\2A> . 'F:\iutCours\2A\Scripts\PowerShell\TP2\script.ps1'
    Votre nombre : 1
    La valeur saisie est égale à 1

    F:\iutCours\2A> . 'F:\iutCours\2A\Scripts\PowerShell\TP2\script.ps1'
    Votre nombre : 3
    La valeur saisie est égale à 2

    F:\iutCours\2A> . 'F:\iutCours\2A\Scripts\PowerShell\TP2\script.ps1'
    Votre nombre : 12
    la valeur n'est pas égale à 1, ni à 2, ni à 3
    ```

3. Même exercice mais avec la commande switch et en allant jusque 5 :

    ```console
    Votre nombre : 6
    la valeur saisie n'est pas comprise entre 1 et 5
    Votre nombre : 3
    la valeur saisie est égale à 3
    ```

    **Script:**

    ```powershell
    [int]$nb = Read-Host "Votre nombre"
    switch($name){
        1 {
            "La valeur saisie est égale à 1"
        }
        2 {
            "La valeur saisie est égale à 2"
        }
        3 {
            "La valeur saisie est égale à 3"
        }
        4 {
            "La valeur saisie est égale à 4"
        }
        5 {
            "La valeur saisie est égale à 5"
        }
        default{
            "La valeur saisie n'est pas comprise dans 1, 2, 3, 4, 5"
        }
    }
    ```

    **Résultat:**

    ```txt
    F:\iutCours\2A> . 'F:\iutCours\2A\Scripts\PowerShell\TP2\script.ps1'
    Votre nombre : 12
    La valeur saisie n'est pas comprise dans 1, 2, 3, 4, 5

    F:\iutCours\2A> . 'F:\iutCours\2A\Scripts\PowerShell\TP2\script.ps1'
    Votre nombre : 5
    La valeur saisie est égale à 5
    ```

<div style="page-break-after: always; visibility: hidden"> \pagebreak </div>

# 5. Exercice 5 : les fonctions

1. Entraînez vous à créer des fonctions.
    Par exemple, créer une fonction Bonjour qui affichera "Bonjour, nous sommes le samedi 4 mars 2023", en utilisant la date du système, bien sûr !

    **Script:**

    ```powershell
    function Bonjour {
        $date = Get-Date
        Write-Host "Bonjour, nous sommes le $($date.ToString('dddd d MMMM yyyy'))"
    }

    Bonjour
    ```

    **Résultat:**

    ```txt
    PS F:\iutCours\2A> . 'F:\iutCours\2A\Scripts\PowerShell\TP2\script.ps1'
    Bonjour, nous sommes le mercredi 8 mars 2023
    ```

2. Fonction avec arguments : dans un script, reprenez l'exercice 4.3 dans une fonction et appelez ensuite cette fonction en passant l'entier en argument :

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

    **Script:**

    ```powershell
    function maFunc($nb) {
        switch ($nb) {
            1 {
                "La valeur saisie est égale à 1"
            }
            2 {
                "La valeur saisie est égale à 2"
            }
            3 {
                "La valeur saisie est égale à 3"
            }
            4 {
                "La valeur saisie est égale à 4"
            }
            5 {
                "La valeur saisie est égale à 5"
            }
            default {
                "La valeur saisie n'est pas comprise dans 1, 2, 3, 4, 5"
            }
        }
    }

    maFunc(1)
    maFunc(3)
    maFunc(5)
    maFunc(6)
    ```

    **Résultat:**

    ```txt
    PS F:\iutCours\2A> . 'F:\iutCours\2A\Scripts\PowerShell\TP2\script.ps1'
    La valeur saisie est Ã©gale Ã  1
    La valeur saisie est Ã©gale Ã  3
    La valeur saisie est Ã©gale Ã  5
    La valeur saisie n'est pas comprise dans 1, 2, 3, 4, 5
    ```

3. Créez une fonction moyenne (en précisant le nom des paramètres) qui retourne la moyenne de 2 nombres. L'appel de la fonction devra préciser le nom des paramètres.

    * Exemple d'appel de la fonction : `moyenne -nb1 15 -nb2 20`
    * Exemple de résultat : `La moyenne de 15 et 20 est de 17.5`

    **Script:**

    ```powershell
    function Moyenne {
        param (
            [Parameter(Mandatory = $true)]
            [double]$nb1,

            [Parameter(Mandatory = $true)]
            [double]$nb2
        )

        $moyenne = ($nb1 + $nb2) / 2
        Write-Host "La moyenne de $nb1 et $nb2 est de $moyenne"
    }

    Moyenne -nb1 15 -nb2 20
    Moyenne 15 17
    ```

    **Résultat:**

    ```txt
    PS F:\iutCours\2A> . 'F:\iutCours\2A\Scripts\PowerShell\TP2\script.ps1'
    La moyenne de 15 et 20 est de 17.5
    La moyenne de 17 et 15 est de 16  
    ```

**Validation : Faites valider votre fonction `moyenne` à l'enseignant encadrant**

# 6. Exercice 6 : Génération de nombre « aléatoires » dans testFonction.ps1

* Dans un script nommé `testFonction.ps1` définissez une fonction nommée nbAlea qui utilise une instance de l’objet system.random pour retourner un nombre aléatoire. Le programme principal sera composé d’une boucle `for` effectuant 10 appels à la fonction `nbAlea` et qui affiche le nombre retourné.

    ```powershell
    $random = New-Object System.Random
    function nbAlea {
        return $random.Next()
    }

    for ($i = 0; $i -lt 10; $i++) {
        $aleatoire = nbAlea

        Write-Host $aleatoire
    }
    ```

* Définissez ensuite une autre fonction qui teste si un nombre est pair ou impair.

    ```powershell
    function parite([int]$nb) {
        return $nb % 2 -eq 0
    }
    ```

* Testez votre fonction dans votre boucle.

    ```powershell
    $random = New-Object System.Random
    function nbAlea {
        return $random.Next()
    }

    function parite([int]$nb) {
        return $nb % 2 -eq 0
    }

    for ($i = 0; $i -lt 10; $i++) {
        $aleatoire = nbAlea
        $pair = parite $aleatoire

        Write-Host "$aleatoire $pair"
    }
    ```

    ```txt
    PS F:\iutCours\2A> . 'F:\iutCours\2A\Scripts\PowerShell\TP2\testFonction.ps1'
    1896289495 False   
    1832987922 True    
    1166140787 False   
    677967662 True     
    2075603889 False   
    1867722928 True    
    1597660704 True    
    264120637 False    
    1625601083 False   
    286920832 True 
    ```

* Modifiez votre programme pour que la fonction `nbAlea` accepte un paramètre correspondant au nombre de nombres aléatoires à générer. L’itération s’effectuera donc dans la fonction `nbAlea`.

    ```powershell
    $random = New-Object System.Random
    function nbAlea($nb) {
        for ($i = 0; $i -lt $nb; $i++) {
            Write-Host $random.Next()
        }
    }

    function parite([int]$nb) {
        return $nb % 2 -eq 0
    }


    nbAlea 10
    ```

    ```txt
    PS F:\iutCours\2A> . 'F:\iutCours\2A\Scripts\PowerShell\TP2\testFonction.ps1'
    414847001 
    951694868 
    489275292 
    308906772 
    2135136463
    1003756650
    283112699
    1922089073
    1598470573
    412417613
    ```

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

**Script:**

```powershell
function saisieEmail {
    $entree = Read-Host("Saisir email")

    return $entree -like "*@*.*"
}

function saisieEmailRegex {
    $entree = Read-Host("Saisir email")

    return $entree -match '^([a-zA-Z0-9._%+-]+|"[^"]+")@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(\.[a-zA-Z]{2,})?$'
}

$valide = $false
do {
    $valide = saisieEmail
}while (-not $valide)
```

**Résultat:**

```txt
PS F:\iutCours\2A> . 'F:\iutCours\2A\Scripts\PowerShell\TP2\testInteraction.ps1'
Saisir email: email
Saisir email: email@test
Saisir email: email@test.com
```

**Validation : Faites valider votre script `testInteraction.ps1` à l'enseignant encadrant**

<div style="page-break-after: always; visibility: hidden"> \pagebreak </div>

# 8. Exercice 8 : Un script complet

1. Proposez un script `liste.ps1` prenant en paramètre un nom de dossier et affichant son contenu.

    ```powershell
    if ($args.Count -eq 0) {
        Write-Host "Veuillez spécifier un nom de dossier en tant que paramètre."
    }
    else {
        $dossier = $args[0]

        if (Test-Path $dossier -PathType Container) {
            Get-ChildItem $dossier
        }
        else {
            Write-Host "Le dossier '$dossier' n'existe pas."
        }
    }

    ```

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

    **Script:**

    ```powershell
    if ($args.Count -eq 0) {
        Write-Host "Veuillez spécifier un nom de dossier en tant que paramètre."
    }
    else {
        $dossier = $args[0]

        if (Test-Path $dossier -PathType Container) {
            $elements = Get-ChildItem $dossier
            foreach ($element in $elements) {
                if ($element.PsIsContainer) {
                    Write-Host "Répertoire : $($element.Name)"
                }
                else {
                    Write-Host "Fichier : $($element.Name)"
                }
            }
        }
        else {
            Write-Host "Le dossier '$dossier' n'existe pas."
        }
    }

    ```

    **Résultat:**

    ```txt
    PS F:\iutCours\2A> . 'F:\iutCours\2A\Scripts\PowerShell\TP2\liste.ps1' F:\iutCours\2A\Scripts\PowerShell\TP2\test
    Répertoire : test2   
    Fichier : a copy 2.txt
    Fichier : a copy 3.txt
    Fichier : a copy 4.txt
    Fichier : a copy.txt  
    Fichier : a.txt
    ```

3. Complétez le script précédant pour que le paramètre du nom de dossier soit nommé dir et que le script accepte un second paramètre nommé filtre permettant de demander l’affichage des fichiers ou des dossiers.
    Voici un exemple d’invocation de votre script `liste.ps1`

    ```console
    .\liste.ps1 –dir C:\ -filtre fichier
    .\litse.ps1 –dir C:\ -filtre dossier
    ```

    **Script:**

    ```powershell
    [CmdletBinding()]
    param (
        [Parameter(Mandatory = $true)]
        [string]$dir,

        [Parameter()]
        [string]$filtre = "tout"
    )

    if (Test-Path $dir -PathType Container) {
        $elements = Get-ChildItem $dir
        foreach ($element in $elements) {
            if ($filtre -in "tout", "dossiers" -and $element.PsIsContainer) {
                Write-Host "Répertoire : $($element.Name)"
            }
            elseif ($filtre -in "tout", "fichiers" -and -not $element.PsIsContainer) {
                Write-Host "Fichier : $($element.Name)"
            }
        }
    }
    else {
        Write-Host "Le dossier '$dir' n'existe pas."
    }

    ```

    **Résultat:**

    ```txt
    PS F:\iutCours\2A> . 'F:\iutCours\2A\Scripts\PowerShell\TP2\liste.ps1' -dir F:\iutCours\2A\Scripts\PowerShell\TP2\test
    Répertoire : test2   
    Fichier : a copy 2.txt
    Fichier : a copy 3.txt
    Fichier : a copy 4.txt
    Fichier : a copy.txt  
    Fichier : a.txt       
    PS F:\iutCours\2A> . 'F:\iutCours\2A\Scripts\PowerShell\TP2\liste.ps1' -dir F:\iutCours\2A\Scripts\PowerShell\TP2\test -filtre fichiers
    Fichier : a copy 2.txt
    Fichier : a copy 3.txt
    Fichier : a copy 4.txt
    Fichier : a copy.txt  
    Fichier : a.txt       
    PS F:\iutCours\2A> . 'F:\iutCours\2A\Scripts\PowerShell\TP2\liste.ps1' -dir F:\iutCours\2A\Scripts\PowerShell\TP2\test -filtre dossiers
    Répertoire : test2
    ```

**Validation : Faites valider votre script `liste.ps1` à l'enseignant encadrant**

# 9. Exercice 9 : Un peu de style

Colorer sa console... Powershell vous permet d'agir sur la console à travers l'objet `host.ui.RawUI`

* Listez les propriétés de cet objet.
    **Commande:**

    ```powershell
    $Host.UI.RawUI | Get-Member -MemberType Property
    ```

    **Résultat:**

    ```powershell
    PS F:\iutCours\2A> $Host.UI.RawUI | Get-Member -MemberType Property


    TypeName : System.Management.Automation.Internal.Host.InternalHostRawUserInterface

    Name                  MemberType Definition
    ----                  ---------- ----------
    BackgroundColor       Property   System.ConsoleColor BackgroundColor {get;set;}
    BufferSize            Property   System.Management.Automation.Host.Size BufferSize {get;set;}
    CursorPosition        Property   System.Management.Automation.Host.Coordinates CursorPosition {get;set;}
    CursorSize            Property   int CursorSize {get;set;}
    ForegroundColor       Property   System.ConsoleColor ForegroundColor {get;set;}
    KeyAvailable          Property   bool KeyAvailable {get;}
    MaxPhysicalWindowSize Property   System.Management.Automation.Host.Size MaxPhysicalWindowSize {get;}    
    MaxWindowSize         Property   System.Management.Automation.Host.Size MaxWindowSize {get;}
    WindowPosition        Property   System.Management.Automation.Host.Coordinates WindowPosition {get;set;}
    WindowSize            Property   System.Management.Automation.Host.Size WindowSize {get;set;}
    WindowTitle           Property   string WindowTitle {get;set;}
    ```

* Changez la couleur de fond de votre fenêtre ainsi que la couleur de votre texte.

**Script:**

```powershell
$Host.UI.RawUI.ForegroundColor = "Blue"
$Host.UI.RawUI.BackgroundColor = "White"

Write-Host "Wow : Couleurs"

$Host.UI.RawUI.ForegroundColor = "Gray"
$Host.UI.RawUI.BackgroundColor = "Black"

Write-Host "Oh les anciennes."
```

<div style="page-break-after: always; visibility: hidden"> \pagebreak </div>

***

![Creative Commons](images/88x31.png)

[Ce document est mis à disposition selon les termes de la Licence Creative Commons Attribution - Pas d'Utilisation Commerciale - Pas de Modification 4.0 International](http://creativecommons.org/licenses/by-nc-nd/4.0/)

 IUT Lannion © 2023 by R&T is licensed under CC BY-NC-ND 4.0
