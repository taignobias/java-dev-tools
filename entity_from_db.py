import datetime
import sys
import argparse
import csv

parser=argparse.ArgumentParser(description='Generate Model java class from csv file')
parser.add_argument('-o', metavar='output', nargs=1, default="model.java", help='Designate output class (default: name of input file)')
parser.add_argument('input', help='Designate input file')

if len(sys.argv[1:])==0:
    parser.print_help()
    parser.exit()

args = parser.parse_args()

model="model"

modelrebuild = args.input.split("_")
jmodel=""
i=0
for subs in modelrebuild:
    subs=subs.lower()
    subs=subs.capitalize()
    jmodel += subs
    i+=1
jmodel="".join(jmodel)

infile = open(args.input, "r")
if args.o[0] is 'm':
    model=jmodel
    outfile=open(model + ".java", "w")
else:
    outfile = open(args.o[0] + ".java", "w")
    model=args.o[0]
reader=csv.reader(infile)
tabdepth=0
d=dict()

memcount=0

#Read infile
for row in reader:
    if reader.line_num is 1:
        outfile.write("@Entity\n")
        outfile.write("@Table(name=\""+model+"\")\n")
        outfile.write("public class " + model + " {\n")
    else:
        memcount+=1
        key=row[0]
        if "varchar" in row[1]:
            value="String"
        elif "integer" in row[1]:
            value="int"
        elif "bigint" in row[1]:
            value="long"
        elif "timestamp" in row[1]:
            value="Timestamp"
        elif "char" in row[1]:
            value="char"
        else:
            value=row[1]
        outfile.write("\t/// " + "   ".join(row) + "\n")
        outfile.write("\t@Column(name=\"" + key + "\")\n")
        #Transform key into camel case without underscores - important for java libraries
        fulltext = key.split("_")
        correctkey = ""
        for text in fulltext:
            text=text.lower()
            text=text.capitalize()
            correctkey+=text
        correctkey="".join(correctkey)
        correctkey=correctkey[0].lower() + correctkey[1:]
        #print the new value as a private member
        outfile.write("\tprivate " + value + " " + correctkey + ";\n")
        d[correctkey] = value

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
    if i+1 < memcount:
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
