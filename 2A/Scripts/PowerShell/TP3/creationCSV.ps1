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