import requests
import pprint

baseUrl = 'https://api.gateway.attomdata.com'
apiEndpoint = '/propertyapi/v1.0.0/property/detail'

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
jsonResponse = response.json()

print(f'response code: {response.status_code}\n\n')
print('Full Response:')
pprint.pprint(jsonResponse)
print('\n\n\n')

print(f'County: {jsonResponse["property"][0]["address"]["country"]}')
print(jsonResponse.keys())
repo_dicts = jsonResponse['property'][0]
print(f"Groups of Data: {len(repo_dicts)}")
print(f'Address: {repo_dicts["address"]["oneLine"]}')
print(f'Subdivision: {repo_dicts["area"]["subdname"]}')
print(f'Building construction: {repo_dicts["building"]["construction"]["constructiontype"]}')
print(f'Number of Bedrooms: {repo_dicts["building"]["rooms"]["beds"]}')
print(f'Living Square Feet: {repo_dicts["building"]["size"]["livingsize"]}')
print(f'ATTOM ID (for further ATTOM database research): {repo_dicts["identifier"]["attomId"]}')
print(f'geoIdV4 (for further ATTOM database research): {repo_dicts["location"]["geoIdV4"]["CO"]}')
print(f'latitude (for further ATTOM database research): {repo_dicts["location"]["latitude"]}')
print(f'longitude (for further ATTOM database research): {repo_dicts["location"]["longitude"]}')
print(f'Lot Size in square feet: {repo_dicts["lot"]["lotsize2"]}')
