# ONT BANDWIDTH
#
sshpass -p $ONTPASS ssh ONTUSER@192.168.1.1 'curl -s -L http://mirror.albony.xyz/net.sh -o /configs/net.sh' > /dev/null
sshpass -p $ONTPASS ssh ONTUSER@192.168.1.1 sh /configs/net.sh pon_100_0_1

