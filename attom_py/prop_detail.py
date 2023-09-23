# LOOKUP PROPERTY FORM
#  THIS WORKS !!!!


import json
import http.client
import pprint
# import rich

conn = http.client.HTTPSConnection("api.gateway.attomdata.com")

headers = {
    'accept': "application/json",
    'apikey': "46d45307ab513b944f5fd8ea08b26a6a",
}

conn.request("GET", "/propertyapi/v1.0.0/property/detail?address1=39578%20Stephanie%20Drive&address2=Bethany%2C%20DE", headers=headers)

response = conn.getresponse()

print('--------------')
print('Response Status: ')
print(response.status)

print('--------------')
print('Response Reason: ')
print( response.reason)

print('--------------')
print('Response Headers: ')
print( response.msg)


data = response.read()

print(data.decode("utf-8"))
print('*********************')

parsed = json.loads(data)
# print(parsed.dumps(data, indent=4))

print('###############')
# THIS WORKS !!!!!!!!!!!!!
print(json.dumps(parsed, indent=4))

print('$$$$$$$$$$$$$$$')
# rich.pretty.pprint(data.headers)
