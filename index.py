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
      print(item)
      if ("last" in self.xjson[item].keys()):
        # Havelock
        value =  float(self.xjson[item]['last'])
        ticks = item
        returnparse.append([ticks, value])
      elif ("last_price" in self.xjson[item].keys()):
        # Crypto Stocks
        value = float(self.xjson[item]['last_price'])
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
        # Add Currency Code to those with no Currency Code (e.g. Havelock)
        if "currency" not in unparsedlong[item].keys():
          # Assume non defined are Bitcoin
          self.mysecurities[item]["currency"] = "BTC"
        # Run through Items
        for individualitems in unparsedlong[item].keys():
          if (individualitems in [ "name", "symbol", "units", "currency", "ticker", "number_public_shares" ]):
            # Only grab the info that I want
            '''
              Mappings for Various Markest (This is where the Magic is :(
              Us        Havelock      CryptoStocks
              name      "name"        "name"
              symbol    "symbol"      "ticker"
              units     "units"       "number_public_shares"
              currency   BTC(H)       "currency"  
            '''
            # Do Bindings
            if (individualitems == "ticker"):
              # Bind Ticker to Symbol
              self.mysecurities[item]["ticker"] = unparsedlong[item][individualitems]
            elif (individualitems == "number_public_shares"):
              # Bind number_public_shares to units
              self.mysecurities[item]["units"] = unparsedlong[item][individualitems]
            else:
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
    

