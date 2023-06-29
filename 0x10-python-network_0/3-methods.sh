#!/bin/bash
# this script displays all methods an Http server will accept
curl -sIX OPTIONS "$1"  | grep 'Allow' | sed 's/Allow: //p' | uniq
