import os
import sys
from lib.path import (LAB_PATH, LAB_FOLDERS)

def mklab(name):
    for f in LAB_FOLDERS:
        try:
            os.makedirs(os.path.join(LAB_PATH, name, f))
            print(f"{f} Successfully created in {os.path.join(LAB_PATH, name)}")
        except FileExistsError:
            print(f"{f} Already exists in {os.path.join(LAB_PATH, name)}")

def rmlab(name):
    _ask(f"Do you really want to remove folder {name}? [y/n]: ")
    _rmlab(name)

def _ask(prompt): 
    while True:
        print(prompt)
        res = input()
        if res == 'y':
            break
        elif res == 'n':
            sys.exit()

def _rmlab(name):
    raise Exception("This feature is currently disabled")