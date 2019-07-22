import datetime
import sys
import argparse
import csv

parser=argparse.ArgumentParser(description='Generate Model java class from csv file')
parser.add_argument('-o', nargs=1, metavar='output', default="model.java", help='Designate output file name [default: model.java]')
parser.add_argument('input', help='Designate input file')

if len(sys.argv[1:])==0:
    parser.print_help()
    parser.exit()

args = parser.parse_args()

infile = open(args.input, "r")
if args.o[0] is 'm':
    outfile=open(args.input + ".java", "w")
else:
    outfile = open(args.o[0], "w")
reader=csv.reader(infile, delimiter="\t")
tabdepth=0
d=dict()
objname="model"

memcount=0

#Read infile
for row in reader:
    if reader.line_num is 1:
        outfile.write("package " + row[0] + ";\n\n")
    elif reader.line_num is 2:
        model=row[0]
        outfile.write("public class " + model + " {\n")
        tabdepth=1
    else:
        memcount+=1
        key=row[1]
        value=row[0]
        d[key] = value
        if len(row) >= 3:
            outfile.write("\t///" + row[2] + "\n")
        outfile.write("\tprivate " + value + " " + key + ";\n")

#Create all private data members
infile.close()

outfile.write("\n")

#Create default constructor
outfile.write("\tpublic " + model + "() {\n")
for key,value in d.items():
    outfile.write("\t\tthis." + key + " = null;\n")
outfile.write("\t}\n")

i=0

#Create more complex constructor
outfile.write("\n\tpublic " + model + "(\n")
for key,value in d.items():
    outfile.write("\t\t" + value + " " + key )
    if i < memcount:
        outfile.write(",")
        i+=1
    outfile.write("\n")
outfile.write("\t\t)\n\t{\n")
for key,value in d.items():
    outfile.write("\t\tthis." + key + " = " + key + ";\n")
outfile.write("\t}\n")

#Create getters and setters
for key,value in d.items():
    outfile.write("\n\tpublic " + value + " get" + key + "() {\n")
    outfile.write("\t\treturn this." + key + ";\n")
    outfile.write("\t}\n")
    outfile.write("\tpublic void set" + key + " (" + value + " " + key + ") {\n")
    outfile.write("\t\tthis." + key + " = " + key + ";\n")
    outfile.write("\t}\n")

outfile.write("\n}")
outfile.close()
