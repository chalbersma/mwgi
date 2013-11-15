#!/usr/bin/env python3
import json
import urllib.request
import logging
import time
import datetime
import csv
import sys

def getbighavk(HAVKStocks):
	api = "https://www.havelockinvestments.com/api/index.php?cmd=ticker&symbol="
	url = api 
	#print(HAVKStocks)
	# Get Current Value
	request = urllib.request.Request(api, headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:24.0) Gecko/20100101 Firefox/24.0'})
	response = urllib.request.urlopen(request)
	xjson = json.loads((response.read().decode('utf-8')))
	#print(xjson)
	returnhavk = []
	# Show Values
	for item in HAVKStocks:
		value =  (int(float(xjson[item[0]]['last'])  * float(100000000)))
		ticks = item[0]
		returnhavk.append([ticks, value])
	return (returnhavk)


