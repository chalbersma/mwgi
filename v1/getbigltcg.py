#!/usr/bin/env python3
import json
import urllib.request
import logging
import time
import datetime
import csv
import sys

from getltcbtc import getltcbtc

def getbigltcg(LTCGStocks):
	api = "https://www.litecoinglobal.com/api/ticker"
	url = api 
	#print(HAVKStocks)
	# Get Current Value
	request = urllib.request.Request(api, headers = {'user-agent': 'MWGI'})
	response = urllib.request.urlopen(request)
	xjson = json.loads((response.read().decode('utf-8')))
	#print(xjson)
	convert = getltcbtc()
	returnltcg = []
	# Show Values
	for item in LTCGStocks:
		value =  (int(float(convert) * float(xjson[item[0]]['last_price'])  * float(100000000)))
		ticks = item[0]
		returnltcg.append([ticks, value])
	return (returnltcg)


