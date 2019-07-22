'''

Write timestamped journal entries

Author: Robert Beisert
Version: 1.0.0
Date: April 12, 2018


'''

from datetime import datetime
from pytz import timezone

#format = "%H:%M"

#now_here = datetime.now(timezone('America/Chicago'))
#print (now_here.strftime(format))


closes=0;
format = "%H:%M"
while(closes==0):
    stored = input(">  ")
    if((stored is "quit") or (stored is "q") or (stored is "QUIT") or (stored is "Q")):
        closes=1
    else:
        journal = open(".journal.jrn", "a")
        now_here = datetime.now(timezone('America/Chicago'))
        journal.write(now_here.strftime(format))
        journal.write("\t")
        journal.write(stored)
        journal.write("\n")
        journal.close()
