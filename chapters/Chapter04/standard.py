from ncclient import manager

router = manager.connect(
    username='expert',
    password='1234QWer!',
    host='192.168.255.52',
    hostkey_verify=False
)

payload = '''
<config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
      <ip>
        <access-list>
          <standard xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-acl">
            <name>Pod16_Task043</name>
            <access-list-seq-rule>
              <sequence>5</sequence>
              <permit>
                <std-ace>
                  <host-address>203.0.113.2</host-address>
                  <host>203.0.113.2</host>
                </std-ace>
              </permit>
            </access-list-seq-rule>
          </standard>
        </access-list>
      </ip>
    </native>
</config>
'''

payload_bgp = '''
<config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
    <router>
      <bgp xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-bgp">
        <id>12345</id>
        <neighbor>
          <id>2.3.4.5</id>
          <remote-as>3356</remote-as>
        </neighbor>
      </bgp>
    </router>
  </native>
</config>
'''

payload_ospf = '''
<config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
      <router>
        <router-ospf xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-ospf">
          <ospf>
            <process-id>
              <id>1</id>
              <network>
                <ip>192.168.254.0</ip>
                <wildcard>0.0.0.255</wildcard>
                <area>1</area>
              </network>
            </process-id>
          </ospf>
        </router-ospf>
      </router>
    </native>
    </config>
'''

router.edit_config(payload_ospf, target='running')