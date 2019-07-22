import datetime
import sys
import argparse
import re
import os
import shutil

VersionNumber="1.1"

parser=argparse.ArgumentParser(description='Update version numbers for system(in format Release:Major:minor version)')
parser.add_argument('-f', metavar='forced-version', nargs=1, help='Force version number')
parser.add_argument('-M', action='store_true', help='Next Major Version')
parser.add_argument('-R', action='store_true', help='Next Release Number')
parser.add_argument('-m', action='store_true', help='Increment Minor Version Number')
parser.add_argument('input', help='Designate input directory')

if len(sys.argv[1:])==0:
    parser.print_help()
    parser.exit()

args = parser.parse_args()
pattern = re.compile("[0-9]+\.[0-9]+\.[0-9]+")
rep_pattern = re.compile("^[0-9]+\.[0-9]+\.[0-9]+$")
rootDir=args.input

print("Running version " + VersionNumber)

for dirName, subdirList, fileList in os.walk(rootDir):
    for fName in fileList:
        changeflag=0
        if 'pom.xm' in fName:
            inName = os.path.join(dirName,fName)
            outName = os.path.join(dirName,fName + ".new")
            infile = open(inName, "r")
            outfile= open(outName,"w")
            print(os.path.join(dirName,fName))
            for line in infile:
                if (("<groupId>" in line) or ("<artifactId>" in line)) and ("mgmw" in line):
                    print(line)
                    changeflag=1
                elif (("<groupId>" in line) or ("<artifactId>" in line)) and not ("mgmw" in line):
                    changeflag=0
                if "<version>" in line:
                    try:
                        if changeflag > 0:
                            cur_version = pattern.search(line).group(0)
                            if args.R:
                                t_ver_vals = cur_version.split('.')
                                t_minor = int(t_ver_vals[0])
                                t_minor += 1
                                t_ver_vals[0] = str(t_minor)
                                t_ver_vals[1] = '0'
                                t_ver_vals[2] = '0'
                                cur_version = '.'.join(t_ver_vals)
                            elif args.M:
                                t_ver_vals = cur_version.split('.')
                                t_minor = int(t_ver_vals[1])
                                t_minor += 1
                                t_ver_vals[1] = str(t_minor)
                                t_ver_vals[2] = '0'
                                cur_version = '.'.join(t_ver_vals)
                            elif args.m or len(sys.argv[1:])==1:
                                t_ver_vals = cur_version.split('.')
                                t_minor = int(t_ver_vals[2])
                                t_minor += 1
                                t_ver_vals[2] = str(t_minor)
                                cur_version = '.'.join(t_ver_vals)
                            elif args.f is not None:
                                if pattern.search(args.f[0]):
                                    cur_version = args.f[0]
                            else:
                                pass
                            if rep_pattern.search(cur_version):
                                line = re.sub(pattern, cur_version, line)
                            print(line)
                    except:
                        pass
                    changeflag=0
                outfile.write(line)
            infile.close()
            outfile.close()
            shutil.copy(outName,inName)
            os.remove(outName)
        elif ".html" in fName:
            inName = os.path.join(dirName,fName)
            outName = os.path.join(dirName,fName + ".new")
            infile = open(inName, "r", errors="ignore")
            outfile= open(outName,"w")
            print(os.path.join(dirName,fName))
            for line in infile:
                if ("MGMW REST API" in line):
                    print(line)
                    try:
                            cur_version = pattern.search(line).group(0)
                            if args.R:
                                t_ver_vals = cur_version.split('.')
                                t_minor = int(t_ver_vals[0])
                                t_minor += 1
                                t_ver_vals[0] = str(t_minor)
                                t_ver_vals[1] = '0'
                                t_ver_vals[2] = '0'
                                cur_version = '.'.join(t_ver_vals)
                            elif args.M:
                                t_ver_vals = cur_version.split('.')
                                t_minor = int(t_ver_vals[1])
                                t_minor += 1
                                t_ver_vals[1] = str(t_minor)
                                t_ver_vals[2] = '0'
                                cur_version = '.'.join(t_ver_vals)
                            elif args.m or len(sys.argv[1:])==1:
                                t_ver_vals = cur_version.split('.')
                                t_minor = int(t_ver_vals[2])
                                t_minor += 1
                                t_ver_vals[2] = str(t_minor)
                                cur_version = '.'.join(t_ver_vals)
                            elif args.f is not None:
                                if pattern.search(args.f[0]):
                                    cur_version = args.f[0]
                            else:
                                pass
                            if rep_pattern.search(cur_version):
                                line = re.sub(pattern, cur_version, line)
                            print(line)
                    except:
                        pass
                outfile.write(line)
            infile.close()
            outfile.close()
            shutil.copy(outName,inName)
            os.remove(outName)
        elif "GlobalConstants.java" in fName:
            inName = os.path.join(dirName,fName)
            outName = os.path.join(dirName,fName + ".new")
            infile = open(inName, "r")
            outfile= open(outName,"w")
            print(os.path.join(dirName,fName))
            for line in infile:
                if ("VERSION_NUMBER" in line):
                    print(line)
                    try:
                            cur_version = pattern.search(line).group(0)
                            if args.R:
                                t_ver_vals = cur_version.split('.')
                                t_minor = int(t_ver_vals[0])
                                t_minor += 1
                                t_ver_vals[0] = str(t_minor)
                                t_ver_vals[1] = '0'
                                t_ver_vals[2] = '0'
                                cur_version = '.'.join(t_ver_vals)
                            elif args.M:
                                t_ver_vals = cur_version.split('.')
                                t_minor = int(t_ver_vals[1])
                                t_minor += 1
                                t_ver_vals[1] = str(t_minor)
                                t_ver_vals[2] = '0'
                                cur_version = '.'.join(t_ver_vals)
                            elif args.m or len(sys.argv[1:])==1:
                                t_ver_vals = cur_version.split('.')
                                t_minor = int(t_ver_vals[2])
                                t_minor += 1
                                t_ver_vals[2] = str(t_minor)
                                cur_version = '.'.join(t_ver_vals)
                            elif args.f is not None:
                                if pattern.search(args.f[0]):
                                    cur_version = args.f[0]
                            else:
                                pass
                            if rep_pattern.search(cur_version):
                                line = re.sub(pattern, cur_version, line)
                            print(line)
                    except:
                        pass
                outfile.write(line)
            infile.close()
            outfile.close()
            shutil.copy(outName,inName)
            os.remove(outName)
