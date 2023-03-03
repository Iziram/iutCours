# Initialisation de la variable $nombre
$nombre = -1

# Boucle do...while pour demander à l'utilisateur de saisir un nombre entre 0 et 10
do {
    # Demande à l'utilisateur de saisir un nombre
    $nombre = Read-Host "Entrez un nombre entre 0 et 10 : "
} while (($nombre -lt 0 )-or ($nombre -gt 10) )

# Affichage du nombre saisi par l'utilisateur
Write-Output "Vous avez saisi le nombre : $nombre"
