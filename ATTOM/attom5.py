import urllib

import requests
from requests import HTTPError
import json
import http.client
import pprint


print('##############')
print("Second ATTOM Example")
print('##############')

headers = {
    'accept': "application/json",
    'apikey': "070c9bc6097eff64f82dc7a55fcb480f",
}

#  Base ATTOM URL
conn = http.client.HTTPSConnection("api.gateway.attomdata.com")

url_ext = "/propertyapi/v1.0.0/property/detail?"

street_num = '100'
street_name = 'Main St'
City = "Bethany"
St = "DE"

url_dict = {"street_num": '100',
            "street_name": 'Main St',
            "city": 'Bethany',
            "St": 'DE',
            }



'''
street_num = input('Street Number?')
street_name = input('Street Name?')
city = input('City?')
state = input('State?')
address1 = street_num + " " + street_name
print("\n address1: ")
print(address1)
address2 = " " + city + ", " + state
print("\n address2: ")
print(address2)
print("\n")
'''
address1 = street_num + " " + street_name
address2 = " " + city + ", " + state

print("^^^^^^^^^^^")
print('address1 urlencoded:')
params1 = (urllib.parse.quote(address1))
print(params1)

print("===========")
params2 = (urllib.parse.quote(address2))
#  produces:  'Bethany%20Beach%2C%20DE'
print('address2 urlencoded:')
print(params2)
print("\n")

# Need to create a dictionary
urldict = {}
urldict["address1"] = address1
urldict["address2"] = address2
print(urldict)
print("\n")

print(" urllib.parse.urlencode()   adds + and = and &   %20 is space, %25 is %")
params3 = urllib.parse.urlencode(urldict)  # BROKEN
print("PARAMS3: ")
print(params3)


conn.request("GET", )  # ERROR HERE

print('##############')
print("THIS WORKS")
print('##############')
# this works -->
# conn.request("GET", "/propertyapi/v1.0.0/property/detail?address1=39578%20Stephanie%20Drive&address2=Bethany%2C%20CO", headers=headers)



res2 = conn.getresponse()
data = res2.read()
print(data.decode("utf-8"))

print('##############')
print("Results Details")
print('##############')
z = json.loads(data)
print('json: ')
print(z["status"])
print('variable y is: ')
print(type(z))
print('$$$$$$$$$$')

# json.dumps(data, indent=4)
print('print(y.items())[0]')
print(z.items())
print(z)
print("BREAK")
# this works --> pprint.pprint(z)
