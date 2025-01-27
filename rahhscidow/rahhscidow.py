#!/usr/bin/env python
# coding: utf-8


import os
import glob
import subprocess
import importlib.util

# parse the doi list
def read_strings_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            # Read all lines from the file, strip newline characters, and create a list
            string_list = [line.strip() for line in file.readlines()]
        return string_list
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []

# invoke sci-hub to download the paper
def call_module(module_name, args=None):
    command = [module_name] + (args if args else [])
    subprocess.run(command)

#check latest paper´s name
#def get_latest_file(directory):
    # Get all files in the directory
    #files = glob.glob(os.path.join(directory, '*'))
    #if not files:
    #    print("No files found in the directory.")
    #    return None

    # Get the file with the latest modification time
    #latest_file = max(files, key=os.path.getmtime)
    #return latest_file


def main():
    print("""
               
                                                     
    
    
               _     _              _     _               
              | |   | |            (_)   | |              
     _ __ __ _| |__ | |__  ___  ___ _  __| | _____      __
    | '__/ _` | '_ \| '_ \/ __|/ __| |/ _` |/ _ \ \ /\ / /
    | | | (_| | | | | | | \__ \ (__| | (_| | (_) \ V  V / 
    |_|  \__,_|_| |_|_| |_|___/\___|_|\__,_|\___/ \_/\_/  
                                                          
                                                          
    © Artur Toloknieiev, 2024
                                                    
    
    
    """)
    file_path = input("Yield DOI list: ") 
    target_path = input("Yield target directory: ")
    scihub_mirror = input("Yield scihub mirror in https://[link_name] format or leave empty for default: ").strip()
    if not scihub_mirror:
        scihub_mirror = "https://www.sci-hub.wf/"
    strings_list = read_strings_from_file(file_path)
    
    
    spec = importlib.util.find_spec('sci-hub')
    if spec is not None:
        print('Dependencies OK.')
    else:
        call_module("pip", ["install", "sci-hub"])
    
    
    # pulled the file renamer
    for element in strings_list:
        if element == "":
            continue
        try:
            call_module("scihub", ['-s', f'{element}', "-O", f"{target_path}", "-u", f"{scihub_mirror}"])
        except Exception as e:
            print(str(e))
    print("Paper retrieval done")

if __name__ == "__main__":
    main()




