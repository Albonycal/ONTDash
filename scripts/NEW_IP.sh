#!/bin/bash

echo "[+] Restarting PPPoE Daemon [+]"

## CFGCLI DISABLE PPP CON
sshpass -p $ONTPASS ssh ONTUSER@192.168.1.1 cfgcli -s InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANPPPConnection.1.Enable false
sleep 1s

## CFGCLI ENABLE PPP CON

sshpass -p $ONTPASS ssh ONTUSER@192.168.1.1 cfgcli -s InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANPPPConnection.1.Enable true

echo "[+] Getting new IP from BNG [+]"


