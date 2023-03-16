param (
    [string]$csvFile
)



if (-not (Test-Path $csvFile)) {
    Write-Host "Le fichier CSV spécifié n'existe pas."
    exit
}

. C:\Users\Matthias\Desktop\IUT\iutCours\2A\Scripts\PowerShell\TP3\gestionGroupe.ps1 -action -create etudiant
. C:\Users\Matthias\Desktop\IUT\iutCours\2A\Scripts\PowerShell\TP3\gestionGroupe.ps1 -action -create enseignant

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

            . C:\Users\Matthias\Desktop\IUT\iutCours\2A\Scripts\PowerShell\TP3\gestionGroupe.ps1 -action -addUser $username $user.role

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

    
