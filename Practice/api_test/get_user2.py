
import requests

p = {"page":2}
resp = requests.get("https://reqres.in/api/users",params=p)
print (resp.url)
jsonresp = resp.json()
print (jsonresp['total_pages'])
assert (jsonresp['total_pages']) == 2, "Value not matching"
assert (jsonresp["data"][0]['email']).endswith("reqres.in"), "email id in not matching"
print(jsonresp['support']['url'])
