# Tell Me Who Are You
create ansible inventory automatically by install agent on servers

## What is TMWAY

The `TMWAY` is REST application written by Flask that accepts some data from linux servers and makes ansible inventory based on these information.

### Usage:
It's simple, you just need made POST request method under `/tmway` prefix and then your inventory will be created on `inventory/hosts.ini` file. like this example:

When application starts on docker container, you can see logs like this:
```asd
PATTERN_CONFIG_FILE = /config/hostname_pattern.yml
INVENTORY_FILE = /inventory/hosts.ini
TMWAY is available on http://172.22.0.2:5000/tmway
```
now we can send servers data with curl to tmway server:
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

To customization hosts.ini based on your hostnames, you can define your hostname patterns in [hostname_pattern.yml](config/hostname_pattern.yml)
```pattern.yml
patterns:
- '([wW]eb[sS]erver)'
- '([sS]erver)'
- '(clusterA)'
```

by first regex group matching, group name added to inventory for example:
`- '([wW]eb[sS]erver)' will match with every host names in hostnames list = [webserver1, groupB-webserver2-frontend, WebServer, webServer02, yyyWebServerxxx]`
Then these hostnames will be set on that group on inventory


You can build docker image from [Dockerfile](Dockerfile)
```dockerfile
docker build -t inventory_generator:latest .
```
