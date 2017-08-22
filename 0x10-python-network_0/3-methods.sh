#!/bin/bash
# displays the allowed methods the server will accept
curl -sI "$1" | grep Allow | cut -c8-
