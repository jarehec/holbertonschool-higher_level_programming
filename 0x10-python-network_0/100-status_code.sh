#!/bin/bash
#displays the status code of the server's response
curl -s -o /dev/zero -w "%{http_code}" "$1"
