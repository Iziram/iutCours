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