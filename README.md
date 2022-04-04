# Tell Me Who Are You
Create ansible inventory automatically by installing agent on servers

The main purpose of this application is to use on [ansible-cmdb stack](https://github.com/miladpav/cmdb-stack)

## What is TMWAY

The `TMWAY` is a REST application written by Flask that accepts some data from Linux servers and makes ansible inventory based on this information.

### Detail:
It's simple, you just need to make a POST request method under the `/tmway` prefix and then your inventory will be created on the `inventory/hosts.ini` file. like this example:

When the application starts on the docker container, you can see logs like this:
```logs
PATTERN_CONFIG_FILE = /config/hostname_pattern.yml
INVENTORY_FILE = /inventory/hosts.ini
TMWAY is available on http://172.22.0.2:5000/tmway
```
Now we can send servers data with curl to tmway server:
```agent.sh
curl -X POST -H "Content-Type: application/json" -d '{"IP", "192.168.20.50". "hostname": "HOSTNAME2"}' http://172.22.0.2:5000/tmway
```
Server output in logs:
```server.log
Hostname HOSTNAME2 with IP Address 192.168.20.50, This Request gets from 192.168.20.50
192.168.20.50 - - [2021-12-17 13:38:59] "POST /tmway HTTP/1.1" 200 184 0.007833
```

Client output in stdout:
```client.stdout
{"message":"your ip address added to inventory successfully","status":"ok"}
```

Inventory after few requests on server will be like this:
```hosts.ini
[uncategorized]
HOSTNAME1 ansible_host=127.0.0.1
HOSTNAME2 ansible_host=192.168.20.50
HOSTNAME3 ansible_host=10.10.20.30

[clusterA]
clusterA-Server1 ansible_host=192.168.1.1
clusterA-Server2 ansible_host=192.168.1.2

[webserver]
webserver1 ansible_host=192.168.1.5
webserver2 ansible_host=192.168.1.6
```

To customization [hosts.ini](inventory/hosts.ini.sample) based on your hostnames, you can define your hostname patterns in [hostname_pattern.yml](config/hostname_pattern.yml)
```pattern.yml
patterns:
- '([wW]eb[sS]erver)'
- '([sS]erver)'
- '(clusterA)'
```

By first regex group matching, group name added to the inventory for example:
`- '([wW]eb[sS]erver)' will match with every hostnames in hostnames list = [webserver1, groupB-webserver2-frontend, WebServer, webServer02, yyyWebServerxxx]`
Then these hostnames will be set on that group on inventory

An effective way of using this application is to put [agent.sh](agent.sh) to your terraform config files or virtualization OVF template as a cron job because when server take its own IP address that can send their information to tmway server, also tmway create inventory automatically and after that, you have all servers IP address which can be a target of Ansible playbooks

Example of using this service in `docker-compose`:
```docker-compose.yml
version: "3.8"
services:
  tmway:
    image: miladpav/inventory_generator:latest
    container_name: tmway
    hostname: tmway
    environment:
      - "HTTP_PORT=5000"
      #- "HTTP_PROTOCOL=http"
      #- "TMWAY_PREFIX=tmway"
      #- "INVENTORY_FILE=/inventory/hosts.ini"
      #- "PATTERN_CONFIG_FILE=/config/hostname_pattern.yml"
    volumes:
      - $PWD/inventory:/inventory
      - $PWD/config:/config
    ports:
      - "5000:5000"

```
