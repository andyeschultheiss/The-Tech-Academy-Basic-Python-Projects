## Title: txtCheck.py
##
## Author: Andy Schultheiss
##
## Date: 14 April 2020
##
## Description: Script checks a user-designated folder for ".txt" files and
##              prints their filenames and modified timestamps to the console
##
## Python: 3.8.2
##

# using os module
import os
# using pathlib for easy validity check
from pathlib import Path

print("Welcome to the txtCheck script.\n")

def valid_dir():
    # check for valid directory entered
    go = True
    exists = False
    while go or not exists:
        folderpath = input("Please enter a valid folder path.\n>>> ")
        folderpath = Path(folderpath)
        go = not(folderpath.is_dir())
        exists = folderpath.exists()
    return folderpath

def print_out_txt(folderpath):
    with os.scandir(folderpath) as f:
        for entry in f:
            if entry.name.endswith('.txt') and entry.is_file():
                entry_stats = os.stat(os.path.join(folderpath, entry.name))
                entry_mtime = entry_stats.st_mtime
                print(entry.name + "    " + str(entry_mtime))
        f.close()

if __name__ == "__main__":

    folderpath = valid_dir()
    print_out_txt(folderpath)
    
