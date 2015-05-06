#!/usr/bin/python
#
# Keeps your IAP up to date
# Version 0.1

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


def dst_dir():
	global dstdir
	print ''
        print 'Welcome to IAPscrape'
	print ''
	dstdir = raw_input('Enter destination directory: ')
	
	airport_icao()

	return


def iap_K():
	response = urllib2.urlopen(''+url001+''+airport+'').read()
	charts = re.findall('href=[\'"]?([^\'" >]+).PDF',response)

	for pdf in charts:
		pdfs = 'http://airnav.com'+pdf+'.PDF'
		cleanurl = pdfs.strip('http://airnav.com/depart?')
		fullurl = 'http://'+cleanurl+''		
		path = urlparse.urlsplit(fullurl).path
		filename = posixpath.basename(path)
		print 'Downloading:', filename
		response = urllib2.urlopen(fullurl)			
		output = open(''+fullpath+'/'+filename+'','wb')
		output.write(response.read())
		output.close()	
				
	return		


def airport_icao():
	global airport
	global fullpath
	print ''
	airport = raw_input('Enter the four letter ICAO designator of the aiport: ')

	fullpath = ''+dstdir+'/'+airport+''

	if not os.path.exists(fullpath):
	        os.makedirs(fullpath)

	print ''

	iap_K()
	
	return


dst_dir()


# EOF
