import requests

BASE="http://127.0.0.1:5000/"

#response = requests.get(BASE+"helloworld/tim/9")
response = requests.put(BASE+"/video/0")
print(response.json())
#response = requests.post(BASE+"helloworld")
#print(response.json())

