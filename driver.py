#!/usr/bin/env python3.2

# To test the functionality of various classes

from index import stockmarket
from time import sleep

havelock = stockmarket("https://www.havelockinvestments.com/api/index.php?cmd=ticker", "https://www.havelockinvestments.com/r/tickerfull")

print (havelock.stockprices)
print (havelock.mysecurities)

sleep(30)

havelock.updatestockmarket()

print (havelock.stockprices)
print (havelock.mysecurities)