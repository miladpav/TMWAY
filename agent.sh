#!/bin/bash

IP=$(ip a | grep $(ip link | awk -F: '$0 !~ "lo|vir|tun|docker|wl|br|^[^0-9]"{print $2;getline}') -A 5 | grep -Eo '([0-9]*\.){3}[0-9]*' | grep -v '127.0.0' | head -1)
HOSTNAME=$(hostname)
URL=$1

## function
owner_num='50'
check_owner () {
  if [ "${owner_num}" == "14" ]; then
    OWNER_GROUP='PO14'
  elif [ "${owner_num}" == "25" ]; then
    OWNER_GROUP='PO25'
  elif [ "${owner_num}" == "36" ]; then
    OWNER_GROUP='PO36'
  else
    OWNER_GROUP='POInf'
  fi
}

if [ -f /etc/allowed_groups ]; then
  group_count=$(cat /etc/allowed_groups | grep "[oO][pP][eE][rR][aA][tT][iI][oO][nN]" | wc -l)
  if [ ${group_count} == 2 ] || [ ${group_count} == 1 ] || [ ${group_count} -ge 3 ]; then
    owner_num=$(cat /etc/allowed_groups | grep "[oO][pP][eE][rR][aA][tT][iI][oO][nN]" | grep -vi inf | grep -o ..$)
    check_owner
  fi
else
  if [ -f /var/server-configs/server.conf ]; then
    owner_num=$(cat /var/server-configs/server.conf | grep -i "owner" | grep -o ..$)
    check_owner
  fi
fi


if [[ ! -z ${OWNER_GROUP} ]];then
  curl -s -X POST -d "{\"IP\": \"$IP\", \"hostname\": \"$HOSTNAME\", \"owner_group\": \"${OWNER_GROUP}\"}" -H "Content-Type: application/json" "$URL" | tee /tmp/tmway_status.txt
else
  curl -s -X POST -d "{\"IP\": \"$IP\", \"hostname\": \"$HOSTNAME\"}" -H "Content-Type: application/json" "$URL" | tee /tmp/tmway_status.txt
fi
