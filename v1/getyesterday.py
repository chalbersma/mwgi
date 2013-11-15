#!/usr/bin/env python3

import time

def main():

	yesterdaystruct = (time.localtime(time.time()-86400))
	yesterdaystring = str(yesterdaystruct.tm_year) + str(yesterdaystruct.tm_yday)	
	print (yesterdaystring)	

main()
