#!/bin/bash
#displays the status code of the server's response
curl -sI "$1" | grep HTTP | cut -f2 -d' '
