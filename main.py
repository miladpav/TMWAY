from flask import Flask, render_template, request, jsonify
from gevent.pywsgi import WSGIServer
import json, re
from os.path import exists

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main_page():
    return render_template('main_page.html')

@app.route('/tmway', methods=['GET', 'POST'])
def tmway():
    if request.method == 'POST':
        DATA = json.loads(request.data)
        ip_address = DATA['IP']
        hostname = DATA['hostname']
        print(f"headers: {request.headers}")
        print(f'Hostname is {hostname} and IP Address is {ip_address}, This Request gets from {request.remote_addr}')
        
        search_in_hostname = re.search('[FVJ]L(.+?)(CL|ST)', hostname)
        if search_in_hostname:
            group_of_hostname = search_in_hostname.group(1)
            
        if exists('./inventory/hosts.ini'):
            with open('./inventory/hosts.ini', 'r') as inventory:
                content = inventory.readlines()
                
        
        if ip_address == request.remote_addr:
            newHost = f"{hostname} ansible_host={ip_address}\n"
            groupOfHost = f"[{group_of_hostname}]\n"
            if newHost not in content:
                with open('./inventory/hosts.ini', 'a+') as inventory_file:
                    if groupOfHost not in content:
                        inventory_file.write(groupOfHost)
                        inventory_file.write(newHost)
                    else:
                        inventory_file.write(newHost)
                #     #if f"[{group_of_hostname}]\n" in content:
                #     for line in content:
                #         if line == f"[{group_of_hostname}]\n":
                #             line = line + f"{hostname} ansible_host={ip_address}\n"
                #             inventory_file.write(line)
                #         #inventory_file.write(f"{hostname} ansible_host={ip_address}\n")
                # else:
                #     inventory_file.write(f"[{group_of_hostname}]\n")
                #     inventory_file.write(f"{hostname} ansible_host={ip_address}\n")
            return {"status": "ok"}
        else:
            return {"status": "error"}
    else:
        return {"status": "error", "message": "You should request as a POST method with curl"}

        
        
        

       
if __name__ == '__main__':
    print("Webhook is available on http://127.0.0.1:5000\n")
    WSGIServer(('0.0.0.0', 5000), app).serve_forever()
