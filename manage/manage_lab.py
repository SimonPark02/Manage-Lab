import os
import sys
from setting import (LAB_PATH, LAB_FOLDERS)

def mklab(name):
    for f in LAB_FOLDERS:
        try:
            os.makedirs(os.path.join(LAB_PATH, name, f))
            print(f"/{f} Successfully created in /{name}")
        except FileExistsError:
            print(f"/{f} Already exists in /{name}")
    print("May the force be with you ...")

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