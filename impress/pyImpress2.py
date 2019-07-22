import datetime
import sys
import os
import shutil
from time import sleep
import secrets

rootDir="."
while 1 == 1:
    for dirName, subdirList, fileList in os.walk(rootDir):
        for fName in fileList:
            changeflag=0
            if '.xml' in fName or '.html' in fName:
                inName = os.path.join(dirName,fName)
                if 'target' in inName:
                    pass
                else:
                    infile = open(inName, "r", errors='ignore')
                    for line in infile:
                        print(line, end='')
                        sleep(0.025)
                    infile.close()
                    sleep(secrets.randbelow(100)/1000)
