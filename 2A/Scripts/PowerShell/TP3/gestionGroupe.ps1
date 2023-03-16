param (
    [string]$action,
    [string]$nom,
    [string]$utilisateur
)

function CreateSecurityGroup($nom) {
    $exists = Get-LocalGroup -Name $nom -ErrorAction SilentlyContinue
    if (-not $exists) {
        $newGroup = New-LocalGroup -Name $nom -ErrorAction SilentlyContinue
        if ($newGroup) {
            Write-Host "Le groupe de sécurité $nom a été créé avec succès."
        }
        else {
            Write-Host "Échec de la création du groupe de sécurité $nom."
        }
    }
}

function AddUserToGroup($nom_util, $groupName) {
    $util = Get-LocalUser -Name $nom_util -ErrorAction SilentlyContinue
    $group = Get-LocalGroup -Name $groupName -ErrorAction SilentlyContinue

    if ($util -and $group) {
        Add-LocalGroupMember -Group $group -Member $user -ErrorAction SilentlyContinue
        Write-Host "L'utilisateur $nom_util a été ajouté au groupe de sécurité $groupName avec succès."
    }
    elseif (-not $util) {
        Write-Host "L'utilisateur $nom_util n'existe pas."
    }
    else {
        Write-Host "Le groupe de sécurité $groupName n'existe pas."
    }
}


function DeleteSecurityGroup($nom) {
    $exists = Get-LocalGroup -Name $nom -ErrorAction SilentlyContinue
    if ($exists) {
        Remove-LocalGroup -Name $nom -ErrorAction SilentlyContinue
        Write-Host "Le groupe de sécurité $nom a été supprimé avec succès."
    }
}

function ListSecurityGroups() {
    Write-Host "Liste des groupes de sécurité locaux :"
    Get-LocalGroup | Select-Object -Property Name, Description
}

switch ($action) {
    "-create" {
        if ($nom) {
            CreateSecurityGroup $nom
        }
        else {
            Write-Host "Veuillez spécifier le nom du groupe de sécurité à créer."
        }
    }
    "-delete" {
        if ($nom) {
            DeleteSecurityGroup $nom
        }
        else {
            Write-Host "Veuillez spécifier le nom du groupe de sécurité à supprimer."
        }
    }
    "-list" {
        ListSecurityGroups
    }
    "-addUser" {
        if ($nom -and $utilisateur) {
            AddUserToGroup $utilisateur $nom
        }
        else {
            Write-Host "Veuillez spécifier le nom du groupe de sécurité et le nom d'utilisateur."
        }
    }
    default {
        Write-Host "Action non reconnue. Utilisez -create, -delete ou -list."
    }
}
