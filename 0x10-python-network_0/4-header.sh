#!/bin/bash
# this script displays an HTTP response specifict to a header variable
curl -sH "X-School-User-Id:98" "$1"
