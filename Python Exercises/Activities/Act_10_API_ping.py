import requests
res = requests.get("https://api.github.com")
if res.status_code == 200:
    data = res.json()

print(data)



#Your Goal:
#Write a script that uses requests.get() on an API URL, checks if status is 200, and prints the JSON.

import requests
req=requests.get("https://jsonplaceholder.typicode.com/users")
if req.status_code==200:
    data1 = req.json()
    print(data1)
else:
    print(req.status_code)


