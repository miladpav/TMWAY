from flask import Flask, render_template, request
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

        ## Check pattern of hostname and create group base on it
        pattern_list = []
        with open('config/hostname_pattern.conf', 'r') as pattern_file:
            for pattern in pattern_file.readlines():
                if str(pattern)[-1] == '\n':
                    pattern_list.append(pattern[:-1])
                elif str(pattern)[-1] != '\n' and len(str(pattern)) >= 3:
                    pattern_list.append(pattern)
        ## alternative way to read patterns from list hard coded in app
        #pattern_list = ['([wW]eb[sS]erver?)', '([pP]ush[mM][qQ]?)', '(server?)']
        
        ## create group for server_name
        for hostname_pattern in pattern_list:
            if not re.match(hostname_pattern, hostname):
                group_of_hostname = 'uncategorized'
            search_in_hostname = re.search(hostname_pattern, hostname)
            if search_in_hostname:
                group_of_hostname = search_in_hostname.group(1)
                break
            
        ## make buffer of file
        if exists('inventory/hosts.ini'):
            with open('inventory/hosts.ini', 'r') as inventory:
                content = inventory.readlines()

        ## insert data of inventory
        if ip_address == request.remote_addr or 1 == 1:
            newHost = f"{hostname} ansible_host={ip_address}\n"
            groupOfHost = f"[{group_of_hostname}]\n"
            if newHost not in content:
                if groupOfHost not in content:
                    with open('inventory/hosts.ini', 'a+') as inventory_file:
                        # FIXME: this section is not clean, need to improve endlines of file
                        if len(content) != 0:
                            if str(content[-1]) != "\n":
                                inventory_file.write("\n")
                        inventory_file.write(groupOfHost)
                        inventory_file.write(newHost)
                else:
                    Index_of_Group = content.index(groupOfHost)
                    content.insert(Index_of_Group + 1, newHost)
                    with open('inventory/hosts.ini', 'w+') as inventory_file:
                        content = "".join(content)
                        inventory_file.write(content)
            return {"status": "ok", "message": "your ip address added to inventory successfully"}
        else:
            return {"status": "error", "message": "You are not who you said", "claimed_IP": f"{ip_address}", "real_IP": f"{request.remote_addr}"}
    else:
        return {"status": "error", "message": "You should request as a POST method with curl"}

        
        
        

       
if __name__ == '__main__':
    print("Webhook is available on http://127.0.0.1:5000\n")
    WSGIServer(('0.0.0.0', 5000), app).serve_forever()
