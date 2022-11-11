from ncclient import manager

router1_config = open("acl.xml").read()
router1 = manager.connect(host='192.168.255.51', username='expert', password='1234QWer!', hostkey_verify=False)
router1.edit_config(router1_config, target="running")
