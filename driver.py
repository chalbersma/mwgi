#!/usr/bin/env python3

# To test the functionality of various classes

from index import stockmarket
from indice import indice
from time import sleep

havelockinvestments = stockmarket("https://www.havelockinvestments.com/r/tickerfull", "https://www.havelockinvestments.com/r/tickerfull")

havelockinvestments.marketparse()
havelockinvestments.updatestockmarketprices()

print(havelockinvestments.mysecurities)
print(havelockinvestments.stockprices)

cryptostocks = stockmarket("https://cryptostocks.com/api/get_securities_info.json", "https://cryptostocks.com/api/get_securities_info.json")
cryptostocks.marketparse()
cryptostocks.updatestockmarketprices()

print (cryptostocks.mysecurities)
print (cryptostocks.stockprices)

testindexdef = {
                "CRYPTSY" : [cryptostocks],
                "AM1" : [havelockinvestments]
                }
testindex = indice(testindexdef, "Simple")
testindex.pulldata()
