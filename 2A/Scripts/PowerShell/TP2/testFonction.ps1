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