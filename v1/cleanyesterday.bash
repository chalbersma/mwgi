#!/usr/bin/env bash

path="/var/index/data/"
yesterday=`/usr/local/bin/getyesterday.py`
indexes=("mwgi")
for i in ${indexes[@]}
do
	# Old File
	filename="$path$yesterday.${indexes[i]}.today"
	#echo  $filename
	# New File
	newfilename="$path$yesterday.${indexes[i]}.json"
	#echo  $filename
	# Remove last Comma
	lastright=`tail -n 1 $filename`
	head -n -1 $filename > /tmp/index.today
	echo "${lastright%?}" >> /tmp/index.today
	cp /tmp/index.today $filename
	# Add leading bracket
	echo -e "{\"data\":[\n$(cat $filename)" > $filename
	# Add Ending Bracket
	echo ']}' >> $filename
	# Rename File
	mv $filename $newfilename
	# Set correct permissions
	chown www-data:www-data $newfilename
	chmod 664 $newfilename
done
	


