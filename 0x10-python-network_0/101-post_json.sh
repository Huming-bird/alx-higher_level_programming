#!/bin/bash
# this script posts a json file to a server
curl -X POST -d "@$2" "$1"
