import click
from netmiko import ConnectHandler
import json

@click.command()
## Requirement A
@click.option("--single-device", type=str)
##
def collect_config(single_device):
    inventory = json.load(open("inventory.json"))

    devices = {}

    ## Rquirement B
    if single_device and single_device in inventory.keys():
        devices[single_device] = inventory[single_device]
    else:
        devices = inventory
    ##

    for addr, info in devices.items():
        local_config = open(f"running-configs/{addr}.cfg", "r").read()
        remote_config = ""

        ## Requirement C
        net_connect = ConnectHandler(
            host=addr,
            username='expert',
            password='1234QWer!',
            device_type=info['device_type']
        )
        remote_config = net_connect.send_command("show running-config")
        ##

        local_config_lines = local_config.split("\n")
        remote_config_lines = remote_config.split("\n")

        ## Requirement D
        if info["device_type"] == "cisco_ios":
            local_line = [i for i in local_config_lines if 'Last configuration change' in i][0]
            remote_line = [i for i in remote_config_lines if 'Last configuration change' in i][0]
        elif info["device_type"] == "cisco_nxos":
            local_line = [i for i in local_config_lines if 'Running configuration last done' in i][0]
            remote_line = [i for i in remote_config_lines if 'Running configuration last done' in i][0]
        
        local_hash_value = hash(local_line)
        remote_hash_value = hash(remote_line)
        ##

        if local_hash_value != remote_hash_value:
            print(f"Device {addr} has changed.")
            open(f"configs-archive/{addr}.{local_hash_value}.cfg", "w").write(local_config)
            open(f"running-configs/{addr}.cfg", "w").write(remote_config)
        else:
            print(f"Device {addr} has NOT changed.")


if __name__ == "__main__":
    collect_config()
