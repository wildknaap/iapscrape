#!/usr/bin/python
#
# Keeps your IAP up to date
# Version 0.1

import os
import sys
import urllib2
import re


url001 = 'http://airnav.com/airport/'


def error():
        print ''
        print '   Fatal error right in front of screen.'
        print ''

        return


def exit():
        print ''
        print '   You must have hit the wrong any key.'
        print ''

	return


def iap_usa():
	response = urllib2.urlopen(''+url001+''+airport+'').read()
	charts = re.findall('href=[\'"]?([^\'" >]+).PDF',response)

	for pdf in charts:
		print 'http://airnav.com'+pdf+'.PDF'
			
	return		


def airport_icao():
	global airport
	print ''
	print 'Welcome to IAPscrape'
	print ''
	airport = raw_input('Enter the four letter ICAO designator of the aiport: ')

	iap_usa()
	
	return


#class aip(scrapy.Charts):
#	url = scrapy.Field()
	





airport_icao()


# EOF
