from netmiko import ConnectHandler
from ntc_templates.parse import parse_output
import netaddr

class InvalidRouteException(Exception):
    pass

device_type = "cisco_ios"
host = "192.168.255.52"
username = "expert"
password = "1234QWer!"

net_connect = ConnectHandler(
## Requirement A
    device_type=device_type,
    host=host,
    username=username,
    password=password
##
)

## Requirement B
static_nexthop_ip = "10.202.16.2"
static_vrf = "challenge-202-pod-16"
##

## Requirement C
out = net_connect.send_command(f"show ip route vrf {static_vrf} static")
parsed_output = parse_output(
    command = f"show ip route vrf {static_vrf} static",
    data=out,
    platform=device_type
)
print(parsed_output)
##

print("Current static routes:")
for i in range(0, len(parsed_output)):
    route = parsed_output[i]
    if route['nexthop_ip'] == static_nexthop_ip:
        address = netaddr.IPNetwork(f"{route['network']}/{route['mask']}")
        print(f"Route number {i}: {route['network']}/{address.netmask} -> {route['nexthop_ip']}")

print()
action = ''
while action not in ['delete', 'add']:
    action = input('Add or delete route: ')

if action == 'delete':
    i = int(input('Which route number to delete: '))

    ## Requirement D
    myroute = parsed_output[i]
    address = netaddr.IPNetwork(f"{myroute['network']}/{myroute['mask']}")
    delete_command = f"no ip route vrf {static_vrf} {myroute['network']} {address.netmask} {static_nexthop_ip}"
    net_connect.send_config_set([delete_command])
    ##

    print("Route deleted!")
elif action == 'add':
    network = input('Network: ')
    subnetmask = input('Subnetmask: ')

    ## Requirement E
    if network[:6] != "10.16.":
        raise InvalidRouteException
    if subnetmask[:8] != "255.255.":
        raise InvalidRouteException
    ##

    ## Requirement F
    newroute = f"ip route vrf {static_vrf} {network} {subnetmask} {static_nexthop_ip}"
    net_connect.send_config_set([newroute])
    ##

    print("Route added!")
