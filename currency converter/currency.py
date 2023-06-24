import requests
import json 

url = f"http://api.exchangeratesapi.io/v1/latest?access_key=db0c18c12b283976e7e890f63120934a"

response = requests.get(url)

curr = json.loads(response.text)
print(curr["rates"].keys())

first = input("Enter currency to convert from: ").upper()
second = input("Enter currency to convert to: ").upper()

amount = int(input("Enter amount to convert to: "))

ans =  (amount*curr["rates"][second])//curr["rates"][first]

print(ans)