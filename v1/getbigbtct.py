#!/usr/bin/env python3
import json
import urllib.request
import logging
import time
import datetime
import csv
import sys

def getbigbtct(BTCTStocks):
	api = "https://btct.co/api/ticker"
	url = api 
	#print(HAVKStocks)
	# Get Current Value
	request = urllib.request.Request(api, headers = {'user-agent': 'MWGI'})
	response = urllib.request.urlopen(request)
	xjson = json.loads((response.read().decode('utf-8')))
	#print(xjson)
	returnbtct = []
	# Show Values
	for item in BTCTStocks:
		value =  (int(float(xjson[item[0]]['last_price'])  * float(100000000)))
		ticks = item[0]
		returnbtct.append([ticks, value])
	return (returnbtct)


