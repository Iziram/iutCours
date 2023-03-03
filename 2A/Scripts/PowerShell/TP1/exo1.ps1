Get-WmiObject -Class Win32_Service | ForEach-Object {
    Write-Output $($_.State + " " + $_.Name + " " + $_.Description)
}