# <center>Tell Me Who Are You</center>

## What is TMWAY

The `TMWAY` is REST application written by Flask that accepts some data from linux servers and makes ansible inventory based on these information.

### Usage:
It's simple, you just need made POST request method under `/tmway` prefix and then your inventory will be created on `inventory/hosts.ini` file. like this example:

```agent.sh
curl -X POST -H "Content-Type: application/json" -d '{"IP", "192.168.20.50". "hostname": "HOSTNAME2"}' http://127.0.0.1:5000/tmway
```

```hosts.ini
[uncategorized]
HOSTNAME1 ansible_host=127.0.0.1
HOSTNAME2 ansible_host=192.168.20.50
HOSTNAME3 ansible_host=10.10.20.30

[clusterA]
clusterA-Server1 ansible_host=192.168.1.1
clusterA-Server2 ansible_host=192.168.1.2

[groupB]
groupB-Server1 ansible_host=192.168.1.3
groupB-Server2 ansible_host=192.168.1.4
```

