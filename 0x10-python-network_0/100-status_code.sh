#!/bin/bash
# this script gets only response code without using |
curl -s -o /dev/null -w "%{http_code}" "$1"
