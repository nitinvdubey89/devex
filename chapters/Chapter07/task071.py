from netmiko import ConnectHandler
from ntc_templates.parse import parse_output

rtr = {
    'device_type': 'cisco_nxos',
    'host':   '192.168.255.53',
    'username': 'expert',
    'password': '1234QWer!',
}

net_connect = ConnectHandler(**rtr)

vlan_output = net_connect.send_command('show vlan')
vlan_parsed = parse_output(
    platform = "cisco_nxos",
    command = "show vlan",
    data = vlan_output
)
version_output = net_connect.send_command('show version')
version_parsed = parse_output(
    platform = "cisco_nxos",
    command = "show version",
    data = version_output
)

print(f"The following VLANs was found on switch: {version_parsed[0]['hostname']}")
for v in vlan_parsed:
    print(v['vlan_id'], v['name'])
