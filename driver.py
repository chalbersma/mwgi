#!/usr/bin/env python3.2

# To test the functionality of various classes

from index import stockmarket

havelock = stockmarket("https://www.havelockinvestments.com/api/index.php?cmd=ticker")

print (havelock.stockprices)