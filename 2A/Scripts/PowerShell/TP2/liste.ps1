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
