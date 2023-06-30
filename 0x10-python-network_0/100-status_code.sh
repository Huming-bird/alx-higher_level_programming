#!/bin/bash
# this script gets only response code without using |
grep -Eo "[0-9]+" <<< $(curl -sw %{http_code} "$1")
