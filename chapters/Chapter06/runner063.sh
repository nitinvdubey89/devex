curl -k --silent \
    https://192.168.255.51/restconf/data/Cisco-IOS-XE-native:native/ip/access-list/Cisco-IOS-XE-acl:extended=Pod16_Chapter06 \
    -u expert:1234QWer! \
    -X PUT \
    -H "Content-Type: application/yang-data+json" \
    -H "Accept: application/yang-data+json" \
    -d '{
    "Cisco-IOS-XE-acl:extended": {
        "name": "Pod16_Chapter06",
        "access-list-seq-rule": [
            {
                "sequence": "10",
                "ace-rule": {
                    "action": "permit",
                    "protocol": "udp",
                    "host-address": "198.51.110.1",
                    "dst-host-address": "203.0.113.2",
                    "dst-eq": 123
                }
            }
        ]
    }
}'

