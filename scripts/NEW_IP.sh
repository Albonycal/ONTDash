#!/bin/bash

echo "[+] Restarting PPPoE Daemon [+]"

## CFGCLI DISABLE PPP CON
sshpass -p $ONTPASS ssh -o StrictHostKeyChecking=no ONTUSER@$ONT_IP cfgcli -s InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANPPPConnection.1.Enable false
sleep 1s

## CFGCLI ENABLE PPP CON

sshpass -p $ONTPASS ssh -o StrictHostKeyChecking=no ONTUSER@$ONT_IP cfgcli -s InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANPPPConnection.1.Enable true

echo "[+] Getting new IP from BNG [+]"


