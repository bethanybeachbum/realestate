import requests
import pprint

data = { 'address': '39578 Stephanie Drive, Bethany Beach, DE 19930'
      }


baseUrl = 'https://api.gateway.attomdata.com'
apiEndpoint = '/transportationnoise'

headers = {
  'apikey': "46d45307ab513b944f5fd8ea08b26a6a"
}

params = {
  'address': '39578 Stephanie Drive, Bethany Beach, DE 19930'
}

# Send request, headers and params are both dicts
response = requests.get(url=f'{baseUrl}{apiEndpoint}', headers=headers, params=params)

# Parse full response, returning a dict
jsonResponse = response.json()

print(f'response code: {response.status_code}\n\n')

print('Full Response:')
pprint.pprint(jsonResponse)


print('\n\n\n')
print(f'Noise data for: 39578 Stephanie Drive, Bethany Beach, DE 19930')
print(f'Aviation Noise: {jsonResponse["transportationNoise"]["aviation_noise"]["level_description"]}')
print(f'Emergency Vehicle Noise: {jsonResponse["transportationNoise"]["emg_vehicle_noise"]["level_description"]}')
print(f'Rail Noise: {jsonResponse["transportationNoise"]["rail_whistle_noise"]["level_description"]}')
print(f'Traffic Noise: {jsonResponse["transportationNoise"]["road_noise"]["level_description"]}')
print(f'Traffic Noise Source: {jsonResponse["transportationNoise"]["road_noise"]["noise_sources"][0]["source_description"]}')
# print(f'Average Sales Price: {jsonResponse["salesTrends"][0]["salesTrend"]["avgSalePrice"]}')
# print(f'Out of this Number of Homes: {jsonResponse["salesTrends"][0]["salesTrend"]["homeSaleCount"]}')
#
# print(f'Year: {jsonResponse["salesTrends"][1]["dateRange"]["end"]}')
# print(f'Average Sales Price: {jsonResponse["salesTrends"][1]["salesTrend"]["avgSalePrice"]}')
# print(f'Out of this Number of Homes: {jsonResponse["salesTrends"][1]["salesTrend"]["homeSaleCount"]}')
#
# print(f'Year: {jsonResponse["salesTrends"][2]["dateRange"]["end"]}')
# print(f'Average Sales Price: {jsonResponse["salesTrends"][2]["salesTrend"]["avgSalePrice"]}')
# print(f'Out of this Number of Homes: {jsonResponse["salesTrends"][2]["salesTrend"]["homeSaleCount"]}')
#
