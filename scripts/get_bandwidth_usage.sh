# ONT BANDWIDTH
# This downloads the script responsible for the bandwidth monitor. For some mysterious reasons the built in curl / wget
# Don't work properly with HTTPS, so I am hosting it on my mirror, feel free to check the code, its fairly simple 
#

sshpass -p $ONTPASS ssh ONTUSER@192.168.1.1 'curl -s -L http://mirror.albony.xyz/net.sh -o /configs/net.sh' > /dev/null

# pon_100_0_1 is the interface through which all the traffic to WAN goes 
sshpass -p $ONTPASS ssh ONTUSER@192.168.1.1 sh /configs/net.sh pon_100_0_1

