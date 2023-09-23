import requests
import json
import http.client
# from urllib3 import urlparse
import urllib


host = "api.gateway.attomdata.com"
conn = http.client.HTTPSConnection(host)

headers = { 
    'accept': "application/json", 
    'apikey': "070c9bc6097eff64f82dc7a55fcb480f", 
} 

params = { 
    'address1' : '39578 Stephanie Drive', 
    'address2':'Bethany Beach, DE 19930'} 

import urllib.parse

urllib.parse.urlunparse(host, params)

print('!!!!!!!!!!!!!')
print(host + urllib.urlencode(params))

'''
conn.request("GET", "/propertyapi/v1.0.0/property/detail?address1=39578%20Stephanie%20Drive&address2=Bethany%2C%20DE", headers=headers)
'''



# user input later
# x = input()

import urllib.request
import urllib.parse
from urllib.parse import urlencode, quote_plus

data = {}
data['name'] = 'Somebody Here'
data['location'] = 'Northampton'
data['language'] = 'Python'
url_values = urllib.parse.urlencode(data)
print(url_values)  # The order may differ from below.  
# name=Somebody+Here&language=Python&location=Northampton
url = 'http://www.example.com/example.cgi'
full_url = url + '?' + url_values
data = urllib.request.urlopen(full_url)