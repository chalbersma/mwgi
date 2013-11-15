#!/usr/bin/env python3
import json
import urllib.request
import logging
import time
import datetime
import csv
import sys

def gethavk(ticker):
	api = "https://www.havelockinvestments.com/api/index.php?cmd=ticker&symbol="
	url = api + ticker
	#print(url)
	# Get Current Value
	request = urllib.request.Request(api, headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:24.0) Gecko/20100101 Firefox/24.0'})
	response = urllib.request.urlopen(request)
	xjson = json.loads((response.read().decode('utf-8')))
	#print(xjson)
	# Show Values
	if xjson == 0 :
		# Error
		print("Error: No Value Returned")
		sys.exit(1)
	# Print Value in Satoshis
	return (int(float(xjson[ticker]['last']) * float(100000000)))

