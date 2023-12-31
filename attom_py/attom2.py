'''
Accessing ATTOM DB via python requests
'''
import requests
import pprint

baseUrl = 'https://api.gateway.attomdata.com'
apiEndpoint = '/poisearch/v2.0.0/poi/Street+Address/'

headers = {
  'apikey': "46d45307ab513b944f5fd8ea08b26a6a"
}

params = {
  "address1": "39678 Stephanie Drive",
  "address2": "Bethany Beach, DE"
}

# Send request, headers and params are both dicts
response = requests.get(url=f'{baseUrl}{apiEndpoint}', headers=headers, params=params)

# Parse full response, returning a dict
print(response)
#jsonResponse = response.json()

print(f'response code: {response.status_code}\n\n')
#print('Full Response:')
#pprint.pprint(jsonResponse)
print('\n\n\n')

 #print(f'County: {jsonResponse["property"][0]["address"]["country"]}')
