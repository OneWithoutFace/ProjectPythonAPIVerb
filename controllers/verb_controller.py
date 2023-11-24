from database.__init__ import database
import app_config as config
from flask import jsonify
import requests

def get_verb(data):
    try:
        external_api_url = 'https://lasalle-frenchverb-api-afpnl.ondigitalocean.app/v1/api/verb'
        response = requests.get(external_api_url, headers={'token':
                '278ef2169b144e879aec4f48383dce28e654a009cacf46f8b6c03bbc9a4b9d11'}, json={'verb': data['verb']})
        if(response.status_code == 200):
            return jsonify({"verb": response.json()})
        else:   
            return jsonify({"error": response.json()['errorMessage']})
    except Exception as err:
        print("Error on trying to get a verb",err.json()['errorMessage'])

def random_verb(data):
    try:
        external_api_url = 'https://lasalle-frenchverb-apiafpnl.ondigitalocean.app/v1/api/verb/random'
        response = requests.get(external_api_url, headers={'token':
        '278ef2169b144e879aec4f48383dce28e654a009cacf46f8b6c03bbc9a4b9d11'}, json={'quantity': data['quantity']})
        if(response.status_code == 200):
            return jsonify({"verbs": response.json()})
        else:   
            return jsonify({"error": response.json()['errorMessage']})
    except Exception as err:
        print("Error on trying to get a random verb",err.json()['errorMessage'])