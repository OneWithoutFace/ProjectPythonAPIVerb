import requests
from flask import Blueprint, request, jsonify
import json
from helpers.token_validation import validate_token
from controllers.user_controller import fetch_users

verb = Blueprint("verb", __name__)

# ENDPOINT 1 - GET A SINGLE VERB
@verb.route("/verbs/", methods=["GET"])
def get_single_verb():
    try:
        token = validate_token()

        if token == 400:
            return jsonify({'error': 'Token is missing in the request, please try again'}), 400
        if token == 401:
            return jsonify({'error': 'Invalid token authentication, please login again'}), 401

        try:
            data = json.loads(request.data)

            if 'verb' not in data:
                return jsonify({'error': 'verb is needed in the request.'}), 400
            external_api_url = 'https://lasalle-frenchverb-api-afpnl.ondigitalocean.app/v1/api/verb'
            response = requests.get(external_api_url, headers={'token':
            '278ef2169b144e879aec4f48383dce28e654a009cacf46f8b6c03bbc9a4b9d11'}, json={'verb':
            data['verb']})
            if(response.status_code == 200):
                return jsonify({"verb": response.json()})
            else:   
                return jsonify({"error": response.json()["errorMessage"]})
        except Exception:
            return jsonify({'error': 'Something happened when requesting a verb'}), 500


    except Exception:
        return jsonify({'error': 'Something happened when trying to fetch users.'}), 500

# ENDPOINT 2 - GET A RANDOM VERB
@verb.route("/verbs/random/", methods=["GET"])
def get_random_verb():
    pass

# ENDPOINT 3 - ADD A FAVORITE VERB
@verb.route("/verbs/favorites/", methods=["POST"])
def add_favorite():
    pass

# ENDPOINT 4 - GET A SINGLE FAVORITE VERB
@verb.route("/verbs/favorites/<favoriteUid>/", methods=["GET"])
def get_single_favorite(favoriteUid):
    pass

# ENDPOINT 5 - GET ALL FAVORITE VERBS
@verb.route("/verbs/favorites/", methods=["GET"])
def get_favorites():
    pass

# ENDPOINT 6 - DELETE A FAVORITE VERB BASED ON ID
@verb.route("/verbs/favorites/<favoriteUid>", methods=["DELETE"])
def delete_favorite(favoriteUid):
    pass