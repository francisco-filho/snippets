#!/bin/bash

ip=$(ip addr show eth0 | grep inet  | sed -E 's/(inet\s)([\.0-9]+)\/.*/\2/')
. env/bin/activate
jupyter lab --ip $ip
