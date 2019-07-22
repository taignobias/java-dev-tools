import os
import argparse
import sys
import statistics
import re

def writeIndent(filename, indent, line):
    for i in range(0,indent):
        filename.write("\t")
    filename.write(line)
    filename.write("\n")

parser=argparse.ArgumentParser(description='Count Java lines of Code')
parser.add_argument('root', help='Root directory for this search')

#Print help if no arguments given
if len(sys.argv[1:])==0:
    parser.print_help()
    parser.exit()

args = parser.parse_args()

storefile=open(args.root + "loc", "w")
excelfile=open(args.root + "loc.csv", "w")
indent=0
commentflag=0
totalloc=0
totalcomment=0
totalcount=0
totalFiles=0
totalinclude=0
totalwire=0
filewire=0

annotationPattern = re.compile("^\s*@\w[(\w=)]*\s*$")

avgList = []

for dirName, subDirList, fileList in os.walk(args.root):
    subDirList[:]= [ d for d in subDirList if d not in {"tools","mgmw_toolkit"} ]
    for filename in fileList:
        if ".java" in filename and ("test" not in filename) and ("Test" not in filename):
            writeIndent(storefile, indent, os.path.join(dirName,filename))
            fullpath = os.path.join(dirName,filename)
            fullpath_split = fullpath.split("\\")
            indent+=1
            tempfile=open(os.path.join(dirName,filename), "r", encoding="utf-8", errors='ignore')
            comment=0
            loc=0
            count=0
            include=0
            wired=0
            for row in tempfile:
                count+=1
                if "package" in row:
                    pass
                elif "//" in row:
                    comment+=1
                elif "import" in row:
                    include+=1
                elif "/*" in row:
                    commentflag=1
                    comment+=1
                elif commentflag is 1:
                    if "*/" in row:
                        commentflag=0
                    comment+=1
                elif not row.strip():
                    pass
                elif row.strip() == "{" or row.strip() == "}" or row.strip() == "(" or row.strip() == ")" or row.strip() == ");":
                    pass
                elif annotationPattern.match(row) is not None:
                    wired+=1
                else:
                    loc+=1
            totalloc+=loc
            totalcomment+=comment
            totalcount+=count
            totalwire+=wired
            totalinclude+=include
            totalFiles+=1
            avgList.append(loc)
            if wired > 0:
                filewire+=1
            tempfile.close()
            writeIndent(excelfile, 0, str(len(fullpath_split)) + "," + str(loc))
            writeIndent(storefile, indent, "Lines: " + str(count))
            writeIndent(storefile, indent, "Lines of Code: " + str(loc))
            writeIndent(storefile, indent, "Comments: " + str(comment))
            writeIndent(storefile, indent, "Imports: " + str(include))
            writeIndent(storefile, indent, "Annotations: " + str(wired))
            indent -=1
writeIndent(storefile, indent, "")
writeIndent(storefile, indent, "Files: " + str(totalFiles))
writeIndent(storefile, indent, "Total Lines: " + str(totalcount))
writeIndent(storefile, indent, "Total LOC: " + str(totalloc))
writeIndent(storefile, indent, "Total Comments: " + str(totalcomment))
writeIndent(storefile, indent, "Total Imports: " + str(totalinclude))
writeIndent(storefile, indent, "Total Annotations: " + str(totalwire))
writeIndent(storefile, indent, "")
writeIndent(storefile, indent, "Average Imports per file: " + str(int(totalinclude / totalFiles)))
writeIndent(storefile, indent, "Files with annotations: " + str(filewire))

writeIndent(storefile, indent, "")
writeIndent(storefile, indent, "Mean LoC: " + str(int(totalloc / totalFiles)))
writeIndent(storefile, indent, "Median LoC: " + str(statistics.median(avgList)))
writeIndent(storefile, indent, "Std Dev: " + str(statistics.pstdev(avgList)))

aboveAvg=0
aboveMedian=0
belowAvg=0
belowMedian=0
std1=0
std2=0
std3=0
std4=0
std5=0
stdev=statistics.pstdev(avgList)
avg = int(totalloc/totalFiles)
for entry in avgList:
    if entry > avg:
        aboveAvg+=1
    elif entry < avg:
        belowAvg+=1
    if entry > int(statistics.median(avgList)):
        aboveMedian+=1
    elif entry < int(statistics.median(avgList)):
        belowMedian+=1
    if entry >= int(avg+stdev) and entry < int(avg +(2* stdev)):
        std1+=1
    if entry >= int(avg + (2*stdev)) and entry < int(avg + (3*stdev)):
        std2+=1
    if entry >= int(avg + (3*stdev)) and entry < int(avg + (4*stdev)):
        std3+=1
    if entry >= int(avg + (4*stdev)) and entry < int(avg + (5*stdev)):
        std4+=1
    if entry >= int(avg + (5*stdev)):
        std5 +=1

writeIndent(storefile, indent, "")
writeIndent(storefile, indent, "Above Average: " + str(aboveAvg))
writeIndent(storefile, indent, "Above Median: " + str(aboveMedian))
writeIndent(storefile, indent, "Below Average: " + str(belowAvg))
writeIndent(storefile, indent, "Below Median: " + str(belowMedian))
writeIndent(storefile, indent, "STD +1 (" + str(int(avg + stdev))+ "): " + str(std1))
writeIndent(storefile, indent, "STD +2 (" + str(int(avg + 2*stdev))+ "): " + str(std2))
writeIndent(storefile, indent, "STD +3 (" + str(int(avg + 3*stdev))+ "): " + str(std3))
writeIndent(storefile, indent, "STD +4 (" + str(int(avg + 4*stdev))+ "): " + str(std4))
writeIndent(storefile, indent, "STD +5 or more (" + str(int(avg + 5*stdev))+ "): " + str(std5))

storefile.close()

