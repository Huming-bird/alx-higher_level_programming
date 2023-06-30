#!/bin/bash
# this script gets only response code without using |
grep -Eo '[[:digit:]]{3}' <<< $(curl -sw %{http_code} "$1")
