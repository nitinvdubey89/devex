from ncclient import manager
import json
import xmltodict

payload = '''
<filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <interfaces xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper">
    <interface>
      <name>GigabitEthernet1</name>
      <statistics>
        <in-octets/>
      </statistics>
    </interface>
  </interfaces>
</filter>
'''

m = manager.connect(
    host='192.168.255.52',
    username='expert',
    password='1234QWer!',
    hostkey_verify=False,
    device_params={'name': 'iosxe'})

octets = m.get(payload)
j = xmltodict.parse(octets.xml)
int = j['rpc-reply']['data']['interfaces']['interface']
print(int['name'], int['statistics']['in-octets'])