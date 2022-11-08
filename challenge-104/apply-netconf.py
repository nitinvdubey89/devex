from ncclient import manager

router1_config = open("router1-eigrp.xml").read()
router1 = manager.connect(host='192.168.255.51', username='expert', password='1234QWer!', hostkey_verify=False)
router1.edit_config(router1_config, target="running")

router2_config = open("router2-eigrp.xml").read()
router2 = manager.connect(host='192.168.255.52', username='expert', password='1234QWer!', hostkey_verify=False)
router2.edit_config(router2_config, target="running")
