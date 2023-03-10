#!/bin/sh

sshpass -p $SSHPASS ssh -o StrictHostKeyChecking=no ONTUSER@192.168.1.1 uptime |  cut -d ' ' -f2

