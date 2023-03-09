#!/bin/sh
#add bridge mode and WAN port to the br0 bridge to establish communication with the LAN 
if [ -d "/sys/class/net/br_sfu/lower_eth1" ] && [ -d "/sys/class/net/br_sfu/lower_wan0" ] ; then
    brctl delif br_sfu wan0
    brctl delif br_sfu eth1
    brctl addif br0 eth1
    brctl addif br0 wan0
fi

# if grep RDNSS /etc/radvd.conf; then
#     sed -e '/RDNSS /{N;N;N;d}' /etc/radvd.conf
#     while pgrep /usr/local/sbin/radvd
#     do
#         echo "inside while"
#         kill $(pgrep /usr/local/sbin/radvd)
#         sleep 10
#     done
#     /usr/local/sbin/radvd -C /etc/radvd.conf -m stderr
# fi


if ! grep 'prefix fd19:2168:5024::/64' /etc/radvd.conf; then
     echo "Generating ULA prefix for router advertisements"
     # kill radvd first
     while pgrep /usr/local/sbin/radvd
     do
         echo "inside while"
         kill $(pgrep /usr/local/sbin/radvd)
         sleep 10
     done
    sed -i -e "/^};/d" /etc/radvd.conf

#ULA config
cat <<"EOF">> /etc/radvd.conf
    prefix fd19:2168:5024::/64
    {
        AdvOnLink on;
        AdvAutonomous on;
    };
};
EOF

#manually assign ula and create iptables rules to return all ula traffic back to bro lan devices
    /usr/sbin/ip a a fd19:2168:5024::254/64 dev br0
    ip6tables -D FORWARD_IPV6_PREFIX -s fd19:2168:5024::/64 -i br0 -j RETURN
    ip6tables -I FORWARD_IPV6_PREFIX -s fd19:2168:5024::/64 -i br0 -j RETURN
    /usr/local/sbin/radvd -C /etc/radvd.conf -m stderr
fi
