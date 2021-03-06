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
  
  def updatestockmarketprices(self):
    self.xjson = self.makeapicall()
    self.stockprices = self.priceparse()
    
  def updatestockmarket(self):
    self.lxjson = self.makelongapicall()
    self.mysecurities = self.marketparse()
    
  def marketparse(self):
    infomappings = { 
                "TICKER" : ["name"],
                "FULLNAME" : ["symbol", "ticker"],
                "CURRENCY" : ["currency"],
                "TOTALMARKET" : ["units"],
                }
    
    
    for item in self.lxjson.keys():
      # Grab TICKER for each security
      # Initialize a dict for each security
      self.mysecurities[item] = {}
      for endpoint in self.lxjson[item].keys():
        # Cycle through all the endpoints in each security
        # Cycle through all the mappings
        for mapping in infomappings.keys():
          # if the endpoint is in the mapping you should totally map that shit
          if endpoint in infomappings[mapping]:
            # Place the mapping
            self.mysecurities[item][mapping] = self.lxjson[item][endpoint].encode('utf-8').strip()
    return self.mysecurities
            
  def priceparse(self):
    pricemappings = {
                 "PRICE" : ["last", "last_price"],
                 "CURRENCY" : ["currency"]
                }
    returnparse = {}
    value = 0
    ticks = ""
    currency = "BTC"
    # Cycle through securities by Ticker
    for item in self.xjson.keys():
      # set ticker to item
      ticks = item
      # Cycle through securities' enpoints items name
      for endpoint in self.xjson[item]:
        # if the endpoint are in our mapping it's the price
        if endpoint in pricemappings["PRICE"]:
          # if the price isn't ""
          if self.xjson[item][endpoint] == "" :
            # NO DATA
            value = 0
          else:
            # If the price isn't do the conversion
            # Value Convert to float and store
            value = float(self.xjson[item][endpoint])
          # Currency by default is BTC. Check if this thing has a different currency. If it doesn't then don't do anything but if it does update.
        if endpoint in pricemappings["CURRENCY"]:
          currency = self.xjson[item][endpoint].encode('utf-8').strip()
      # Now that you've found the ticker and he value add it to the price thing
      returnparse[ticks] = [value, currency]
    return returnparse
    
  def __init__(self, api, gapilong):
    # API String to acquire all the tickers
    self.api = api 
    self.apilong = gapilong
    # Item to hold all the stock information
    self.xjson = self.makeapicall()
    self.lxjson = self.makelongapicall()
    self.active = True;
    

