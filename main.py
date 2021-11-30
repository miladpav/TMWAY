from flask import Flask, render_template, request, jsonify
from gevent.pywsgi import WSGIServer
import json


app = Flask(__name__)


@app.route('/', methods=['GET'])
def main_page():
    return render_template('main_page.html')

@app.route('/tmway', methods=['POST'])
def tmway():
    if request.method == 'POST':
        DATA = json.loads(request.data)
        ip_address = DATA['IP']
        hostname = DATA['hostname']
        print(f'Hostname is {hostname} and IP Address is {ip_address}, This Request gets from {request.remote_addr}')
        if ip_address == request.remote_addr:
            return {"status": "ok"}
        else:
            return {"status": "error"}

        
        
        

       
if __name__ == '__main__':
    print("Webhook is available on http://127.0.0.1:5000\n")
    WSGIServer(('0.0.0.0', 5000), app).serve_forever()
