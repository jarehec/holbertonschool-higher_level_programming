#!/usr/bin/env bash
# displays the content length in bytes
curl -sI "$1" | grep Content-Length | cut -f2 -d' ' 
