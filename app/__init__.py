from flask import Flask, render_template, request
from . import pattern, functions
import json

## --------------------------------------------------------------------- ##

app = Flask(__name__)
app.config.from_object('config')


# First Page of application
@app.route('/', methods=['GET', 'POST'])
def main_page():
    if request.method == 'GET':
        return render_template('index.html')

    ## make login here
    elif request.method == 'POST':
        return "login"


prefix = app.config['TMWAY_PREFIX']
# REST accepts servers information and create inventory
@app.route(f'/{prefix}', methods=['GET', 'POST'])
def tmway():
    if request.method == 'POST':

        # check data received or not
        try: 
            DATA = json.loads(request.data)
        except :
            return {"status": "error", "message": "json data not received"}
        
        # check required data received or not
        try:
            DATA['IP']
            DATA['hostname']
        except KeyError:
            return {"status": "error", "message": "Variables 'IP' and 'hostname' must pass in request"}
        else:
            ip_address = DATA['IP']
            hostname = DATA['hostname']
            print(f'Hostname {hostname} with IP Address {ip_address}, This Request gets from {request.remote_addr}')

        invfile = app.config['INVENTORY_FILE']
        pattfile = app.config['PATTERN_CONFIG_FILE']
        
        functions.check_directory(pattfile)
        pattern_list = pattern.pattern_reader(pattfile)
        group_of_hostname = functions.groupCreator(pattern_list, hostname)
        content = functions.make_buffer(invfile)
        
        # TODO: fix remote_addr for reverse proxy situation
        if ip_address == request.remote_addr:
            functions.check_directory(invfile)
            result = functions.insert_line(content, ip_address, hostname, group_of_hostname, invfile)
            return result

        else:
            result = {"status": "error", "message": "You are not who you said", 
                      "claimed_IP": f"{ip_address}", "real_IP": f"{request.remote_addr}"}
            return result
    
    else:
        result = {"status": "error", "message": "You should request as a POST method with curl"}
        return result