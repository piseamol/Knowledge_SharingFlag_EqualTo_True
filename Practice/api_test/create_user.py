import requests


payload = {
    "name": "AP",
    "job": "Automation"
}

postresp = requests.post("https://reqres.in/api/users",data=payload)
print(postresp)
print(postresp.json())
assert postresp.json()['name'] == 'AP1' , "Name not matching"