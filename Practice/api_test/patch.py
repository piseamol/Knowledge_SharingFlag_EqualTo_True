import requests

payload = {
    "name": "PK"
}

putresp = requests.patch("https://reqres.in/api/users/2",data=payload)
print(putresp.json())
assert putresp.json()['name'] == 'PK'