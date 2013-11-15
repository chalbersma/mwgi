#!/usr/bin/env python3

from getbtct import getbtct
from gethavk import gethavk
from getltcg import getltcg
from getbighavk import getbighavk
from getbigbtct	import getbigbtct
from getbigltcg import getbigltcg
 




def mwgi():
	# Still a Test Version of mgwi
	# Going to Grab ASICMINER on each BTC market and CIPHERMINE
	comment = ''' 
	MWGI
	Index Description:
    		Top 25 Stocks in Bitcoin. 
        		"Top 25" Decided By Me.
    		Calculated by adding share price. 
    		Stock must be delivering a product/service.
    		Stock must do significant buisness in BTC.
    		Stock may not be funds.
    		Unless stock is hosted in an unsupported platform/exchange stock may not be passthrough.
    		Currently LTCG BTCT and HAVK only markets accepted.
	Index:
    		1.      AM1             (HAVK)  ("Mining")		    -Passthrough Custom-
    		2.      LTC-GLOBAL      (LTCG)  ("Stock Exchange")
    		3.      BASIC-MINING    (BTCT)  ("Mining")
    		4.      S.MPOE-PT       (BTCT)  ("Stock Exchange")          -Passthrough MPEX.CO-
    		5.      S.BBET          (BTCT)  ("Gambling")                -Passthrough MPEX.CO-
    		6.      CRYPTO-TRADE    (BTCT)  ("Currency Exchange")
    		7.      BITVPS          (BTCT)  ("General Hosting")
    		8.      ESECURITYSABTC  (BTCT)  ("Specialized Hosting")
    		9.      COGNITIVE       (BTCT)  ("Mining")
    		10.     CIPHERMINE      (LTCG)  ("Mining")
    		11.     OPCU            (LTCG)  ("General Hosting")
    		12.     TABITA          (LTCG)  ("Bakery & Other")
    		13.     ART             (LTCG)  ("Ceramic Rentals")
    		14.     S.WIHEE         (LTCG)  ("Other")
    		15.     HIM             (HAVK)  ("Mining")
    		16.     KCIM            (HAVK)  ("Mining")
    		17.     S.MG            (HAVK)  ("Software Development")    -Passthrough MPEX.CO-
    		18.     VTX             (HAVK)  ("Currency Exchange")
    		20.     NASTY-PT        (BTCT)  ("Mining")                  -Passthrough Custom-
    		21.     <OPEN>
    		22.     <OPEN>
    		23.     <OPEN>
    		24.     <OPEN>
    		25.     <OPEN>
	'''
	HAVKStocks = [["AM1",0] , ["HIM",0], ["KCIM",0], ["SMG",0], ["VTX",0] ]
	LTCGStocks = [["LTC-GLOBAL",0] , ["CIPHERMINE",0], ["OPCU",0], ["TABITA",0], ["ART",0], ["S.WIHEE",0]]
	BTCTStocks = [["BASIC-MINING",0], ["S.MPOE-PT",0], ["S.BBET-PT",0], ["CRYPTO-TRADE",0], ["BITVPS",0],\
			["ESECURITYSABTC",0], ["COGNITIVE",0], ["NASTY-PT",0] ]
	HAVKStocks = getbighavk(HAVKStocks)
	LTCGStocks = getbigltcg(LTCGStocks)
	BTCTStocks = getbigbtct(BTCTStocks)
	
	mwgi_value = buildindex(HAVKStocks, LTCGStocks, BTCTStocks)	
	# Remove this Beforehand

	return mwgi_value

def buildindex(HAVKStocks, LTCGStocks, BTCTStocks):
	currentvalue = 0
	for item in HAVKStocks:
		currentvalue = currentvalue + int(item[1])
	for item in LTCGStocks:
		currentvalue = currentvalue + int(item[1])
	for item in BTCTStocks:
		currentvalue = currentvalue + int(item[1])
	return currentvalue

def gethavkstocks(HAVKStocks):
	for item in HAVKStocks:
		item[1] = gethavk(str(item[0]))
	return HAVKStocks

def getltcgstocks(LTCGStocks):
	for item in LTCGStocks:
		item[1] = getltcg(str(item[0]))
	return LTCGStocks

def getbtctstocks(BTCTStocks):
	for item in BTCTStocks:
		item[1] = getbtct(str(item[0]))
	return BTCTStocks

