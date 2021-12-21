import requests

resp = requests.get("https://httpbin.org/delay/3",timeout=2)

assert resp.status_code==200 ,"passed"

#assert resp.status_code!=200 ,"Failed"