#!/bin/sh

sshpass -p $ONTPASS ssh -o StrictHostKeyChecking=no ONTUSER@192.168.1.1 bob ddm

