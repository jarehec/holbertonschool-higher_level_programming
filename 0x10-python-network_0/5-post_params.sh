#!/bin/bash
# sends a header variable with value 98 to the server
curl -d "email=hr@holbertonschool.com" -d "subject=I will always be here for PLD" "$1"
