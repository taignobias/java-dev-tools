import datetime
import sys
import argparse
import csv

parser=argparse.ArgumentParser(description='Generate table html from csv file')
parser.add_argument('-o', metavar='output', nargs=1, default="model.java", help='Designate output class (default: name of input file)')
parser.add_argument('input', help='Designate input file')

if len(sys.argv[1:])==0:
    parser.print_help()
    parser.exit()

args = parser.parse_args()

model="model"

infile = open(args.input, "r")
if args.o[0] is 'm':
    outfile=open(args.input + ".html", "w")
    model=args.input
else:
    outfile = open(args.o[0] + ".html", "w")
    model=args.o[0]
reader=csv.reader(infile, delimiter='\t')
tabdepth=0
d=dict()

memcount=0

outfile.write("<table class=datatable id=" + model + ">\n")

#Read infile
for row in reader:
    outfile.write("<tr>\n")
    if reader.line_num is 1:
        for column in row:
            outfile.write("\t<th>")
            outfile.write(column)
            outfile.write("</th>\n")
    else:
        for column in row:
            outfile.write("\t<td>")
            outfile.write(column)
            outfile.write("</td>\n")
    outfile.write("</tr>\n")
#Create all private data members
infile.close()

outfile.write("</table>\n")

outfile.close()
