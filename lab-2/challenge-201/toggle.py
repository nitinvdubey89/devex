import requests
requests.packages.urllib3.disable_warnings()
import json

restconf_headers = {
    ## Requirement A
    "Accept": "application/yang.data+json",
    "Content-type": "application/yang.data+json"
    ##
}
nexus1_basepath = "https://192.168.255.53/restconf"
expert_auth = requests.auth.HTTPBasicAuth("expert", "1234QWer!")

## Requirement B
rest_endpoint = "/data/Cisco-NX-OS-device:System/intf-items/svi-items/If-list=vlan2116"
##
rsp = requests.get(nexus1_basepath + rest_endpoint, headers=restconf_headers, auth=expert_auth, verify=False).json()
current_status = rsp["If-list"][0]["adminSt"]
print("Current administrative status: " + current_status)


if current_status == "up":
    next_status = "down"
elif current_status == "down":
    next_status = "up"
print("Changing administrative status from " + current_status + " to " + next_status)
rest_endpoint = "/data/Cisco-NX-OS-device:System/intf-items/svi-items/If-list=vlan2116"
body = {
    ## Requirement C
    "adminSt": next_status
    ##
}
requests.patch(nexus1_basepath + rest_endpoint, headers=restconf_headers, auth=expert_auth, verify=False,
    ## Requirement D
    json=body
    ##
    )



## Requirement E
rest_endpoint = "/data/Cisco-NX-OS-device:System/intf-items/svi-items/If-list=vlan2116/adminSt"
##
rsp = requests.get(nexus1_basepath + rest_endpoint, headers=restconf_headers, auth=expert_auth, verify=False).json()
current_status = rsp["adminSt"]
print("Current administrative status: " + current_status)
