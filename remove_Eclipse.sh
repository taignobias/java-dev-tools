find -type d -name .settings > file
find -type f -name .classpath >> file
find -type f -name .project >> file

for file in `cat file`; do
	rm -r $file
done

rm file
