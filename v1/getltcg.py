#!/usr/bin/env python3
import json
import urllib.request
import logging
import time
import datetime
import csv
import sys

def getltcg(ticker):
	api = "https://litecoinglobal.com/api/ticker/"
	url = api + ticker
	#print ("API: " + url)
	# Get Current Value
	request = urllib.request.Request(url)
	response = urllib.request.urlopen(request)
	xjson = json.loads((response.read().decode('utf-8')))
	# Get Conversion Data
	convert = getconversionvalue()
	# Show Values
	# Print Value in Satoshis
	#print (float(convert) * float(xjson['last_price']) * float(100000000))
	return (int(float(convert) * float(xjson['last_price']) * float(100000000)))



def getconversionvalue():
	# Get a number that we can multiple with LTC to get BTC
	url = "https://crypto-trade.com/api/1/ticker/ltc_btc"
	request = urllib.request.Request(url)
	response = urllib.request.urlopen(request)
	xjson = json.loads(response.read().decode('utf-8'))
	return xjson['data']['last']

