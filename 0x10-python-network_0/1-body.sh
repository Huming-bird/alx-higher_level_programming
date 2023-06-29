#!/bin/bash
# this sccript returns the body of a 200code response
res=$(curl -sI "$1" | grep 'HTTP' | cut -d' ' -f2); if [[ $res -eq 200 ]]; then curl -s "$1" -o t && cat t; fi
