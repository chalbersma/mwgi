#!/usr/bin/env python3
import json
import urllib.request
import logging
import time
import datetime
import csv
import sys

def getbtct(ticker):
	api = "https://btct.co/api/ticker/"
	url = api + ticker

	# Get Current Value
	request = urllib.request.Request(url)
	response = urllib.request.urlopen(request)
	xjson = json.loads((response.read().decode('utf-8')))
	# Show Values
	# Print Value in Satoshis
	return (int(float(xjson['last_price']) * float(100000000)))

