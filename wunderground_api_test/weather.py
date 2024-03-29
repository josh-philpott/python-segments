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


	def report_string(self, city, state):

		the_url = self.api_url + self.wu_key + 'conditions/q/' + state.replace(" ", "_") + "/" + city.replace(" ", "_") + '.json'
		response = urllib2.urlopen(the_url)
		json_data = response.read()
		data = json.loads(json_data)
		
		
		if "error" in data['response']:
			print "Error: " + data['response']['error']['type']
			print "Description: " + data['response']['error']['description']
			print city.replace("_"," ") + ", " + state
			return 
		else:

			cur_obv = data['current_observation']

			print "This is the weather report for " + cur_obv['display_location']['full']
			
			#The wunderground API has some terms that don't allow for direct conversationality
			#This is a quick fix for front-end experience
			if cur_obv['weather'] in ["Overcast", "Clear", "Partly Cloudy", "Mostly Cloudy"]:
				print "It is currently " + cur_obv['temperature_string'] + " and " + cur_obv['weather']
			else:
				print "It is currently " + cur_obv['temperature_string'] + " with " + cur_obv['weather']

			print

		


wea = weather()
wea.report_string("Port Orange", "FL")
wea.report_string("Tampa", "FL")
wea.report_string("Fake City", "CA") #not a real city
	
	
