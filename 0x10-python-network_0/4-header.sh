#!/bin/bash
# sends a header variable with value 98 to the server
curl -sH 'X-HolbertonSchool-User-Id:98' "$1"
