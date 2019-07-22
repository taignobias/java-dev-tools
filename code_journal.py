'''

Write timestamped journal entries

Author: Robert Beisert
Version: 1.0.0
Date: April 12, 2018


'''

import argparse
import sys
from datetime import datetime
from datetime import timedelta
from pytz import timezone

def additional_help():
    printmarker=0
    print()


parser = argparse.ArgumentParser(description="Write Coded, timestamped journal entries based on provided codes")
parser.add_argument("code", help="Tag code for the argument")
parser.add_argument("info", help="Information on code (e.g. \"Start\", \"Interrupt\")")

if len(sys.argv[1:])==0:
    parser.print_help()
    additional_help()
    parser.exit()

args=parser.parse_args()

format = "%H:%M"
stored = input(">  ")

journal = open("C:\\cygwin64\\home\\USERNAME\\.journal.jrn", "a")

now_here = datetime.now(timezone('America/Chicago'))

CODE = args.code.upper()
INFO = args.info.upper()

if (CODE == 'DAY') and (INFO == 'S'):
    now_here = now_here - timedelta(minutes=5)
elif CODE == 'DAY' and INFO == 'E':
    now_here = now_here + timedelta(minutes=8)

journal.write(now_here.strftime(format))
journal.write("\t")
journal.write(CODE + "_")
journal.write(INFO + "\t")

journal.write(stored)
journal.write("\n")
journal.close()
