from netmiko import ConnectHandler
from ntc_templates.parse import parse_output

rtr = {
    'device_type': 'cisco_nxos',
    'host':   '192.168.255.53',
    'username': 'expert',
    'password': '1234QWer!',
}

net_connect = ConnectHandler(**rtr)

# vlan_output = net_connect.send_command('show vlan')
# vlan_parsed = parse_output(
#     platform = "cisco_ios",
#     command = "show vlan",
#     data = vlan_output
# )
# version_output = net_connect.send_command('show version')
# version_parsed = parse_output(
#     platform = "cisco_ios",
#     command = "show version",
#     data = version_output
# )

choice = input('Would you like to add or remove a vlan? [add/remove]:')
if choice == 'add':
    vlan_id = input('New VLAN ID: ')
    vlan_name = input('New VLAN name: ')

    create_vlan = [
        f"vlan {vlan_id}",
        f"name {vlan_name}"
    ]
    output = net_connect.send_config_set(create_vlan)
    print("Vlan added!")
elif choice == "remove":
    vlan_id = input('VLAN ID to remove:')

    remove_vlan = [
        f"no vlan {vlan_id}"
    ]
    output = net_connect.send_config_set(remove_vlan)
    print("Vlan removed!")
else:
    print('Bad choice')
