#!/bin/bash
# this script displays the body size of an HTTP header
curl -si "$1" | sed -n 's/Content-Length: \([0-9]\+\)/\1/p'
