#!/bin/sh

sshpass -p $ONTPASS ssh -o StrictHostKeyChecking=no ONTUSER@$ONT_IP uptime |  cut -d ' ' -f2

