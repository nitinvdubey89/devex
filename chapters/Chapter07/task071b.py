from netmiko import ConnectHandler
from ntc_templates.parse import parse_output

rtr = ConnectHandler(
    host='192.168.255.51',
    username='expert',
    password='1234QWer!',
    device_type='cisco_ios'
)

r1 = rtr.send_command('show ip interface brief')

r1_ver = parse_output(
    command = 'show ip interface brief',
    data=r1,
    platform='cisco_ios'
)

print(f"Found {len(r1_ver)} interfaces")

new_loopback = [
    'interface Loopback16094',
    'no shut'
]
r2 = rtr.send_config_set(new_loopback)

r1 = rtr.send_command('show ip interface brief')

r1_ver = parse_output(
    command = 'show ip interface brief',
    data=r1,
    platform='cisco_ios'
)

print(f"Found {len(r1_ver)} interfaces")
