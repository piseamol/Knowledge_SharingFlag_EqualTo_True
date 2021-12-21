
import requests

resp = requests.get("https://reqres.in/api/users?page=2")
#print (resp)
#print(type(resp))
#print(dir(resp))

code = resp.status_code
assert code==200, "Got the 200 OK code"
#print(resp.text)
#print(resp.content)
print(resp.json())
print(resp.headers)
print(resp.cookies)
print(resp.encoding)
print(resp.url)

