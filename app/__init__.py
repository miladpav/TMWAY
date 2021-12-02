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
        return render_template('main_page.html')

    ## make login here
    elif request.method == 'POST':
        return "login"


# REST accepts servers information and create inventory
@app.route('/tmway', methods=['GET', 'POST'])
def tmway():
    if request.method == 'POST':

        # check data received or not
        try: 
            DATA = json.loads(request.data)
        except :
            return {"status": "error", "message": "json data not received"}
        
        # check required data received or not
        try:
            DATA['IP'] and DATA['hostname']
        except NameError:
            return {"status": "error", "message": "Variables \"IP\" and \"hostname\" must pass in request"}
        else:
            ip_address = DATA['IP']
            hostname = DATA['hostname']
            print(f'Hostname {hostname} with IP Address {ip_address}, This Request gets from {request.remote_addr}')

        invfile = app.config['INVENTORY_FILE']
        pattern_list = pattern.pattern_reader(app.config['PATTERN_CONFIG_FILE'])
        group_of_hostname = functions.groupCreator(pattern_list, hostname)
        content = functions.make_buffer(invfile)
        if ip_address == request.remote_addr:
            result = functions.insert_line(content, ip_address, hostname, group_of_hostname, invfile)
            return result

        else:
            result = {"status": "error", "message": "You are not who you said", 
                      "claimed_IP": f"{ip_address}", "real_IP": f"{request.remote_addr}"}
            return result
    
    else:
        result = {"status": "error", "message": "You should request as a POST method with curl"}
        return result