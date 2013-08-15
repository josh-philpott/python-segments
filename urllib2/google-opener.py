#####################################################
# urllib2 examples.
#
# Taken from docs.python.org/2/howto/urllib2.html
#
#####################################################
import urllib2, urllib, sys

# Simplest way to open url and read response

response = urllib2.urlopen('http://google.com/')
html = response.read()

#urlopen(url[,data][,timeout]) can accept URL as string or a Request object

req = urllib2.Request('http://www.google.com')
response = urllib2.urlopen(req)
html = response.read()

#Data can be sent using urllib's urlencode
#This example querys weatherunderground
#http://www.java2s.com/Code/Python/Network/SubmitPOSTData.htm

zipcode = '32128'
url = 'http://www.wunderground.com/cgi-bin/findweather/getForecast'
data = urllib.urlencode({'query': zipcode})
req=urllib2.Request(url)
fd=urllib2.urlopen(req,data)
data=fd.read()
print data
