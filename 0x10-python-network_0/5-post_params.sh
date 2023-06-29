#!/bin/bash
# this script uses a post request to add values to a server
curl -sX POST -d "test=test@gmail.com&subject=I will always be here for PLD" "$1"
