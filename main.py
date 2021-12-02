from flask import Flask, render_template, request, jsonify
from gevent.pywsgi import WSGIServer
import json, re
from os.path import exists


app = Flask(__name__)


@app.route('/', methods=['GET'])
def main_page():
    return render_template('main_page.html')

# TODO: make modular application and seperate functions into seperate files in project tree
@app.route('/tmway', methods=['GET', 'POST'])
def tmway():
    if request.method == 'POST':
        # TODO: check DATA recieved from agent and return proper message for wrong data
        DATA = json.loads(request.data)
        ip_address = DATA['IP']
        hostname = DATA['hostname']
        print(f"headers: {request.headers}")
        print(f'Hostname is {hostname} and IP Address is {ip_address}, This Request gets from {request.remote_addr}')

        # TODO: check uncategorized hosts by their hostname    
        ## check pattern of hostname and create group base on it
        search_in_hostname = re.search('[FVJ]L(.{3,4}?)(CL|ST)', hostname)
        if search_in_hostname:
            group_of_hostname = search_in_hostname.group(1)
            
        ## make buffer of file
        if exists('./inventory/hosts.ini'):
            with open('./inventory/hosts.ini', 'r') as inventory:
                content = inventory.readlines()

        ## insert data of inventory
        if ip_address == request.remote_addr:
            newHost = f"{hostname} ansible_host={ip_address}\n"
            groupOfHost = f"[{group_of_hostname}]\n"
            if newHost not in content:
                if groupOfHost not in content:
                    with open('./inventory/hosts.ini', 'a+') as inventory_file:
                        # FIXME: this section is not clean, need to improve endlines of file
                        if len(content) != 0:
                            if str(content[-1]) != "\n":
                                inventory_file.write("\n")
                        inventory_file.write(groupOfHost)
                        inventory_file.write(newHost)
                else:
                    Index_of_Group = content.index(groupOfHost)
                    content.insert(Index_of_Group + 1, newHost)
                    with open('./inventory/hosts.ini', 'w+') as inventory_file:
                        content = "".join(content)
                        inventory_file.write(content)
            return {"status": "ok"}
        else:
            return {"status": "error"}
    else:
        return {"status": "error", "message": "You should request as a POST method with curl"}

        
        
        

       
if __name__ == '__main__':
    print("Webhook is available on http://127.0.0.1:5000\n")
    WSGIServer(('0.0.0.0', 5000), app).serve_forever()
