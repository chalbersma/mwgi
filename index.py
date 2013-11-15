#!/usr/bin/env python3.2
import json
import urllib.request
import logging
import time
import datetime
import csv
import sys

class stockmarket:

    
  def makeapicall(self):
    request = urllib.request.Request(self.api, headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:24.0) Gecko/20100101 Firefox/24.0'})
    response = urllib.request.urlopen(request);
    apicalljson = json.loads((response.read().decode('utf-8')))
    print (apicalljson.items())
    print (apicalljson.keys())
    print (apicalljson['NEOBEE'])
    return apicalljson
  
  def parsexjson(self):
    print (self.xjson)
    returnparse = []
    value = 0
    ticks = ""
    print (self.xjson['NEOBEE'])
    for item in self.xjson.keys():
      print ()
      value =  (int(float(self.xjson[item]['last']) * float(100000000)))
      ticks = item
      returnparse.append([ticks, value])
    return returnparse
  
  def __init__(self, api):
    # API String to acquire all the tickers
    self.api = api 
    # Item to hold all the stock information
    self.xjson = self.makeapicall()
    self.stockprices = self.parsexjson()