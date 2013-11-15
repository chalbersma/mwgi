#!/usr/bin/env python3


# Includes Here
import time
from acquiremwgi import mwgi

def main():
	# Get Time
	todaystruct =  (time.localtime(time.time()))
	# Convert day into string
	daystring = str(todaystruct.tm_year) + str(todaystruct.tm_yday)
	# Convert minutes into string Prepend 0 if < 10
		# E.G. 9 displayed as 09
	minstring = ""
	if (todaystruct.tm_min < 10):
		minstring = "0" + str(todaystruct.tm_min)
	else:
		minstring = str(todaystruct.tm_min)
	# Build a timestamp string	
		# Note tm_hour will return hour 1 as 1 and not 01
	timestring = str(todaystruct.tm_hour) + minstring
	# Hardcoded file for the data to land
	mwgifile = "/var/index/data/" + daystring + ".mwgi.today"
	# File with index data
	indexs = [["mwgi", mwgifile, mwgi]]
	# Fill all indexes with data
	for item in indexs:
		# open this indexes file in append mode
		# Will create a new file on a new day
		lastprice =  str(item[2]())
		file = open(item[1], 'a')
		# Gather  current data 
			# Note that the item{2] is a funciton that's called to pull data
		towrite = '{"time":' +  timestring + ' ,"price": ' + lastprice + '},\n'
		# write current data to end of file
		file.write(towrite)
		# Close file immediately
		file.close
		lastfile = '/var/index/data/' + str(item[0]) + '_last.json'
		lastwrite = '{"last": {"time":' + timestring +',"price":'+ lastprice + '}}'
		# Open the last file
		file = open(lastfile, 'w')
		file.write(lastwrite)
		file.close
		# Move to next index
		
# Run my program
main()
