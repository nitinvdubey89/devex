from ncclient import manager

router = manager.connect(
    username='expert',
    password='1234QWer!',
    host='192.168.255.51',
    hostkey_verify=False
)

payload = '''
<config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
    <interface>
      <Loopback>
        <name>16042</name>
        <description>Pod16_Task042</description>
        <ip>
          <address>
            <primary>
              <address>10.0.16.41</address>
              <mask>255.255.255.255</mask>
            </primary>
          </address>
        </ip>
      </Loopback>
    </interface>
  </native>
</config>
'''

router.edit_config(payload, target='running')