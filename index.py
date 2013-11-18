#!/usr/bin/env python3.2
import json
import urllib.request
import logging
import time
import datetime
import csv
import sys

class stockmarket:
  
  mysecurities = {}
    
  def makeapicall(self):
    request = urllib.request.Request(self.api, headers = {'user-agent': 'MWGI V2'})
    response = urllib.request.urlopen(request);
    apicalljson = json.loads((response.read().decode('utf-8')))
    return apicalljson
  
  def makelongapicall(self):
    request = urllib.request.Request(self.apilong, headers = {'user-agent': 'MWGI V2'})
    response = urllib.request.urlopen(request);
    apicalljson = json.loads((response.read().decode('utf-8')))
    return apicalljson
  
  def parsexjson(self):
    returnparse = []
    value = 0
    ticks = ""
    for item in self.xjson.keys():
      value =  (int(float(self.xjson[item]['last']) * float(100000000)))
      ticks = item
      returnparse.append([ticks, value])
    return returnparse
  
  def buildsecuritylist(self):
    #
    #{security : { "item1" : item , "item2" : item}
    #
    unparsedlong = self.makelongapicall()
    for item in unparsedlong.keys():
      if (item in self.mysecurities.keys()):
        # Security has already been placed in list 
        # No need to do anything
        continue
      else:
        # Item has not been created
        self.mysecurities[item] = {}
        for individualitems in unparsedlong[item].keys():
          if (individualitems in [ "name", "symbol", "units" ]):
            self.mysecurities[item][individualitems] = unparsedlong[item][individualitems]
            
  def updatestockmarket(self):
    self.xjson = self.makeapicall()
    self.stockprices = self.parsexjson()
        
  def __init__(self, api, gapilong):
    # API String to acquire all the tickers
    self.api = api 
    # Item to hold all the stock information
    self.xjson = self.makeapicall()
    # API String for full market data
    self.apilong = gapilong
    self.stockprices = self.parsexjson()
    self.buildsecuritylist()
    self.active = True;
    

