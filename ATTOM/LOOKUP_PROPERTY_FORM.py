# LOOKUP PROPERTY FORM




import http.client 

conn = http.client.HTTPSConnection("api.gateway.attomdata.com") 

headers = { 
    'accept': "application/json", 
    'apikey': "070c9bc6097eff64f82dc7a55fcb480f", 
} 

conn.request("GET", "/propertyapi/v1.0.0/assessment/detail?postalcode=11215&minAssdTtlValue=1000000&maxAssdTtlValue=2500000&APIKey=070c9bc6097eff64f82dc7a55fcb480f", headers=headers) 

res = conn.getresponse() 
data = res.read() 

print(data.decode("utf-8"))

