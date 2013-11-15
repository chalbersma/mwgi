#!/usr/bin/env python3
#-*- coding: UTF-8 -*-

import cgi
import cgitb
cgitb.enable()
#Custom Imports
from getbtct import getbtct
from gethavk import gethavk
from getltcg import getltcg
from acquiremwgi import mwgi


print("Content-Type:text/html; charset=utf-8\n\n")
print("\n")
print("\n")

def printpage():
	toprintheader = '''\
		<html>
		<head><title>Mid West Guy</title></head>
		
		<body> '''
	dexes=list()
	#Add MWGI
	dexone = mwgi()
	dexes.append("<h2>MWG Index (MWGI)</h2><h3>Satoshis: "+ str(dexone)\
		+ "</h3><h3>Bitcoins: " + str(float(dexone) / float(100000000)))
	
	toprintfooter = "</body></html>"

	toprintbody = ""

	for index in dexes:
		toprintbody = toprintbody + index
 
	toprint = toprintheader + toprintbody + toprintfooter
	return toprint

print(printpage())
