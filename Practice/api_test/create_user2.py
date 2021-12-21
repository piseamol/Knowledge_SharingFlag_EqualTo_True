import requests
import json

mydata = open("data.json").read()
postresp = requests.post("https://reqres.in/api/users",data=json.loads(mydata))
print(postresp)
print(postresp.json())
assert postresp.json()['name'] == 'amit' , "Name not matching"