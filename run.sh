#!/bin/bash
/root/mitm/mitmdump -q --script /root/mitm/server.py --listen-port 8888 --listen-host 0.0.0.0 --allow-hosts '47.114.148.125'
 >> /dev/null
