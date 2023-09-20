import requests
from requests.exceptions import HTTPError


resourceURL = 'https://api.gateway.attomdata.com/propertyapi/v1.0.0/property/detail?'
apiKey = "070c9bc6097eff64f82dc7a55fcb480f"

# address1 = input("What is the street address? ")
# address2 = input("What is the City State and Zipcode? ")

address10 = "105%20Deep%20Bottom%20Place"  #  %2C  is a comma
address20 = "Stephens%20City%2C%20"

response = requests.get(resourceURL)
print(response.status_code)


for url in ['https://api.github.com', 'https://api.github.com/invalid']:
    try:
        response = requests.get(url)
        # If the response was successful, no Exception will be raised
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred:  {http_err}' )  # Python 3.6
    except Exception as err:
        print(f'Other error occurred: {err}')  # Python 3.6
    else:
        print('Success!')

print('response.content:')
print(response.content)
response = requests.get(resourceURL)
print('print response status code')
print(response.status_code)
print('print response content:')
print(response.content)

# resourceURL = 'https://api.gateway.attomdata.com/propertyapi/v1.0.0/property/detail?'
# apiKey = "070c9bc6097eff64f82dc7a55fcb480f"

# address1 = input("What is the street address? ")
# address2 = input("What is the City State and Zipcode? ")

# address10 = "105%20Deep%20Bottom%20Place"  # %2C  is a comma
# address20 = "Stephens%20City%2C%20"
