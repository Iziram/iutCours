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
Moyenne -nb2 15 -nb1 17