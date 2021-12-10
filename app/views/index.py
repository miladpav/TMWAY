from flask import Blueprint, request, render_template
import json


index_api = Blueprint('index_api', __name__)


@index_api.route('/', methods=['GET', 'POST'])
def main_page():
    if request.method == 'GET':
        return render_template('index.html')

    ## make login here
    elif request.method == 'POST':
        return "login"
