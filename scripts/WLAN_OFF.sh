#!/bin/sh
# Nokia CFGCLI

# current status 
echo "Current Status"

sshpass -p $ONTPASS ssh -o StrictHostKeyChecking=no ONTUSER@192.168.1.1  cfgcli -g InternetGatewayDevice.LANDevice.1.WLANConfiguration.1.RadioEnabled
sshpass -p $ONTPASS ssh -o StrictHostKeyChecking=no ONTUSER@192.168.1.1 cfgcli -g  InternetGatewayDevice.LANDevice.1.WLANConfiguration.5.RadioEnabled

sleep 1s

echo "Turning WLAN Radio(s) OFF"

sshpass -p $ONTPASS ssh -o StrictHostKeyChecking=no ONTUSER@192.168.1.1 cfgcli -s InternetGatewayDevice.LANDevice.1.WLANConfiguration.1.RadioEnabled false
sshpass -p $ONTPASS ssh  -o StrictHostKeyChecking=no ONTUSER@192.168.1.1 cfgcli -s  InternetGatewayDevice.LANDevice.1.WLANConfiguration.5.RadioEnabled false
