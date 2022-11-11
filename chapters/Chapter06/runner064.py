import requests
import json

#payload = json.load(open("task064.json", 'r'))
addr = '192.168.255.51'
path = '/data/Cisco-IOS-XE-native:native/ip/access-list/Cisco-IOS-XE-acl:extended=Pod16_Chapter06'
url = f"https://{addr}/restconf{path}"
user='expert'
password='1234QWer!'
headers = {
    'Content-Type': 'application/yang-data+json',
    'Accept': 'application/yang-data+json'
}
r = requests.delete(url, headers=headers, auth=(user,password), verify=False)

print(r.status_code)
print(r.text)
try:
    print(json.dumps(r.json(), indent=2))
except:
    pass