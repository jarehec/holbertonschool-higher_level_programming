#!/bin/bash
#displays the status code of the server's response
curl -sI "$1" | head -n1 | cut -f2 -d' '
