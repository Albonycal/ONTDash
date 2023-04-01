#!/bin/sh

sshpass -p $ONTPASS ssh -o StrictHostKeyChecking=no ONTUSER@$ONT_IP bob ddm

