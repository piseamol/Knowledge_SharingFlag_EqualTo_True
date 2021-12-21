import requests

payload = {
    "name": "PK",
    "job": "Dev3"
}

putresp = requests.put("https://reqres.in/api/users/2",data=payload)
print(putresp.json())
assert putresp.json()['job'] == 'Dev3'