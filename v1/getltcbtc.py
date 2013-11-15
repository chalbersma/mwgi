#!/usr/bin/env python3

import json
import urllib.request
import logging
import time
import datetime
import csv
import sys


def getltcbtc():
	# Get a number that we can multiple with LTC to get BTC
	url = "https://crypto-trade.com/api/1/ticker/ltc_btc"
	value = 0
	request = urllib.request.Request(url)
	response = urllib.request.urlopen(request)
	xjson = json.loads(response.read().decode('utf-8'))
	value =  xjson['data']['last']
	if value == 0:
		# Either the LTC Market has crashed or crypto-trade isn't working
		# Using vicurex
		url = "https://vircurex.com/api/get_last_trade.json?base=LTC&alt=BTC"
		request2 = urllib.request.Request(url, headers = {'user-agent': 'MWGI'})
		response2 = urllib.request.urlopen(request2)
		xjson2 = json.loads(response2.read().decode('utf-8'))
		value = xjson2['value']
	
	return value
