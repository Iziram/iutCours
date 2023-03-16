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
