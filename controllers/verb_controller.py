import requests
from database.__init__ import database
import app_config as config
import bcrypt
import jwt
from datetime import datetime, timedelta
from flask import jsonify

# THIS IS FOR THE FIRST ENDPOINT
def fetch_verb(verbInformation):
    try:
        verb = verbInformation["verb"]
        external_api_url = 'https://lasalle-frenchverb-api-afpnl.ondigitalocean.app/v1/api/verb'
        response = requests.get(
            external_api_url, 
            headers={
                'token': '278ef2169b144e879aec4f48383dce28e654a009cacf46f8b6c03bbc9a4b9d11'
            }, 
            json={
                'verb': verb
            }
        )

        print(verb)

        if response.status_code == 200:
            print(response.status_code)
            return jsonify({'verb': response.json()})
        else:
            print(response.json())
            return 'error'
    
    except Exception as err:
        print("Error: ", err)
    