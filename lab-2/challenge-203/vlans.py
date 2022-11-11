import yaml
from jinja2 import Template
from netmiko import ConnectHandler

net_connect = ConnectHandler(
    device_type = "cisco_nxos",
    host = "192.168.255.53",
    username = "expert",
    password = "1234QWer!"
)

vlan_template = Template(open('vlans.j2').read(), trim_blocks=True, lstrip_blocks=True)
cli_config = vlan_template.render(yaml.safe_load(open('vlans.yaml')))
net_connect.send_config_set(cli_config.split("\n"))
