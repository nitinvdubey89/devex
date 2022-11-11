#!/usr/bin/env bash

## Requirement A
HEADER1='Accept:application/yang.data+json'
HEADER2='Content-Type:application/yang.data+json'
##
NEXUS1_BASEPATH='https://192.168.255.53/restconf'
EXPERT_AUTH="expert:1234QWer!"
#EXPERT_AUTH="mark:mark123^"

## Requirement B
REST_ENDPOINT='/data/Cisco-NX-OS-device:System/intf-items/svi-items/If-list=vlan2116'
##
CURRENT_STATUS=$(curl -k --silent $NEXUS1_BASEPATH$REST_ENDPOINT \
  -u $EXPERT_AUTH \
  -H $HEADER1 \
  -H $HEADER2 \
  | jq '."If-list"[0].adminSt' -r)
echo Current administrative status: $CURRENT_STATUS


if [ "$CURRENT_STATUS" = "up" ]; then
    NEXT_STATUS="down"
else
    NEXT_STATUS="up"
fi
echo Changing administrative status from $CURRENT_STATUS to $NEXT_STATUS
REST_ENDPOINT='/data/Cisco-NX-OS-device:System/intf-items/svi-items/If-list=vlan2116'
## Requirement C
BODY='{"adminSt":"'$NEXT_STATUS'"}'
##
curl -k --globoff -X 'PATCH' \
  $NEXUS1_BASEPATH$REST_ENDPOINT \
  -u $EXPERT_AUTH \
  -H 'Accept: application/yang.data+json' \
  -H 'Content-Type: application/yang.data+json' \
  -d $BODY
## Requirement D
##


## Requirement E
REST_ENDPOINT='/data/Cisco-NX-OS-device:System/intf-items/svi-items/If-list=vlan2116/adminSt'
##
CURRENT_STATUS=$(curl -k --silent $NEXUS1_BASEPATH$REST_ENDPOINT \
  -u $EXPERT_AUTH \
  -H 'Accept: application/yang.data+json' \
  -H 'Content-Type: application/yang.data+json' \
  | jq '.adminSt' -r)
echo Current administrative status: $CURRENT_STATUS
