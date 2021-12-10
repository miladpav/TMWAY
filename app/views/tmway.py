from flask import Blueprint, request
import json
from app import functions

tmway_api = Blueprint('tmway_api', __name__)





# REST accepts servers information and create inventory


@tmway_api.route('/tmway', methods=['GET', 'POST'])
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

        invfile = tmway_api.config['INVENTORY_FILE']
        pattfile = tmway_api.config['PATTERN_CONFIG_FILE']
        
        functions.check_directory(pattfile)
        pattern_list = functions.pattern_reader(pattfile)
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