#!/usr/bin/env python3.2

# To test the functionality of various classes

from index import stockmarket
from time import sleep

havelockinvestments = stockmarket("https://www.havelockinvestments.com/r/tickerfull", "https://www.havelockinvestments.com/r/tickerfull")

havelockinvestments.marketparse()
havelockinvestments.updatestockmarketprices()

print(havelockinvestments.mysecurities)
print(havelockinvestments.stockprices)