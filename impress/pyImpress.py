import datetime
import sys
import os
import shutil
from time import sleep

rootDir="."

while 1 == 1:
    os.system("py.exe ../../_loc_count.py .")
    inName = "./.loc"
    infile = open(inName, "r")
    for line in infile:
        print(line, end='')
        sleep(0.15)
    infile.close()
