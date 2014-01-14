#!/usr/bin/env python3.2

# Object for Indices
from index import stockmarket

class indice:
  '''
    Get my infromation like so:
      itemdefinitions
      {
        stock : [stockmarketobj]
        stock2 : [stockmarketobj]
      }
  '''
  '''
    Store Data like 
    { 
      stock: { marketinfo : [...] , priceinfo : [...] }
      stock: { marketinfo : [...] , priceinfo : [...] }
    }
  '''
  '''
    Models:
      simple
  '''
  def __init__(self, gitemdefinitions, gmodel):
    self.itemdefs = gitemdefinitions
    self.model = gmodel
    
  def pulldata(self):
    itemsdeself = {}
    for item in self.itemdefs.keys():
      marketinfo = self.itemdefs[item][0].mysecurities[item]
      priceinfo = self.itemdefs[item][0].stockprices[item]
      print (marketinfo, priceinfo)
                                    
    
    