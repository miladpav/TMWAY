#!/bin/bash

IP=$(hostname -I | cut -d " " -f1)
HOSTNAME=$1
URL=$2

curl -X POST -d "{\"IP\": \"$IP\", \"hostname\": \"$HOSTNAME\"}" -H "Content-Type: application/json" "$URL"