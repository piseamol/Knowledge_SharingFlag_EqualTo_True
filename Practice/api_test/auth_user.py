
import requests

resp = requests.get("https://the-internet.herokuapp.com/basic_auth",auth=('admin','admin'))
print(resp)

assert resp.status_code == 200, "passed"
#assert resp.status_code != 201, "Failed"
