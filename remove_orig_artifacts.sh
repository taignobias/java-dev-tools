#! /bin/sh

find . -name "*.orig" > remove
cat remove
rm `cat remove`
find . -name "*.orig"
rm remove
