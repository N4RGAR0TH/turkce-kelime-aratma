import http.client
import json


connection = http.client.HTTPSConnection("sozluk.gov.tr")

headers = {
    'content-type': "application/json",
    }

word = input()

connection.request("GET", "/gts?ara=" + word, headers=headers)

res = connection.getresponse()
data = res.read()
parsedData = json.loads(data.decode('utf-8'))

try:
    print(parsedData[0]["anlamlarListe"][0]["anlam"])
except:
    print("Couldn't find any words in the dictionary")