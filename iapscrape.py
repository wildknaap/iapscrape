#!/usr/bin/python
#
# Keeps your IAP up to date
# Version 0.1

dstdir = '/home/pablo/Downloads/test/'


import os
import sys
import urllib2
import re
import os.path
import urlparse
import posixpath

url001 = 'http://airnav.com/airport/'
url002 = 'http://www.ais-netherlands.nl/aim/2015-03-19-AIRAC/eAIP/html/eAIP/EH-AD-2.EHAM-en-GB.html#eham-ad-2.24/'

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


def iap_K():
	response = urllib2.urlopen(''+url001+''+airport+'').read()
	charts = re.findall('href=[\'"]?([^\'" >]+).PDF',response)

	for pdf in charts:
		pdfs = 'http://airnav.com'+pdf+'.PDF'
		#print pdfs.strip( 'http://airnav.com/depart?' )
		cleanurl = pdfs.strip('http://airnav.com/depart?')
		fullurl = 'http://'+cleanurl+''		
		print fullurl
		path = urlparse.urlsplit(fullurl).path
		filename = posixpath.basename(path)
		print filename
		response = urllib2.urlopen(fullurl)			
		output = open(''+dstdir+'/'+filename+'','wb')
		output.write(response.read())
		output.close()
				
	return		


def airport_icao():
	global airport
	print ''
	print 'Welcome to IAPscrape'
	print ''
	airport = raw_input('Enter the four letter ICAO designator of the aiport: ')

	iap_K()
	
	return


#class aip(scrapy.Charts):
#	url = scrapy.Field()
	





airport_icao()


# EOF
