##############################################
# Weather Underground API Test
# 
# Author: Joshua Philpott
#
#############################################

import urllib2, json, my_api_keys

class weather():
	def __init__(self): 
		self.wu_key = my_api_keys.wu_key
       		self.api_url= 'http://api.wunderground.com/api/'
	def report_string(self, state, city):
		#Assuming correct inputs for now
		the_url = self.api_url + self.wu_key + 'conditions/q/' + state + "/" + city + '.json'
		response = urllib2.urlopen(the_url)
		json_data = response.read()
		data = json.loads(json_data)
		
		print the_url

		cur_obv = data['current_observation']

		print "This is the weather report for " + cur_obv['display_location']['full']
		print "It is currently " + cur_obv['temperature_string'] + " with " + cur_obv['weather']


test = weather()
test.report_string("FL", "Port_Orange")
test.report_string("FL", "Tampa")
test.report_string("CA", "Pasadena")
	
	
