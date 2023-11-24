
from flask import Blueprint, request, jsonify
import json
from helpers.token_validation import validate_token
from controllers.verb_controller import get_verb, random_verb

verb = Blueprint("verb", __name__)

# ENDPOINT 1 - GET A SINGLE VERB
@verb.route("/verbs/", methods=["GET"])
def get_single_verb():
    try:
        token = validate_token()

        if token == 400:
            return jsonify({'error': 'Token is missing in the request, please try again'}), 401
        if token == 401:
            return jsonify({'error': 'Invalid token authentication, please login again'}), 403

        try:
            data = json.loads(request.data)

            if 'verb' not in data:
                return jsonify({'error': 'verb is needed in the request.'}), 400
            
            response = get_verb(data)
            return response
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
        except Exception:
            return jsonify({'error': 'Something happened when requesting a verb'}), 500


    except Exception:
        return jsonify({'error': 'Something happened when trying to request a verb'}), 500

# ENDPOINT 2 - GET A RANDOM VERB
@verb.route("/verbs/random/", methods=["GET"])
def get_random_verb():
    try:
        token = validate_token()

        if token == 400:
            return jsonify({'error': 'Token is missing in the request, please try again'}), 401
        if token == 401:
            return jsonify({'error': 'Invalid token authentication, please login again'}), 403
        try:
            data = json.loads(request.data)

            if 'quantity' not in data:
                return jsonify({'quantity': 'quantity is needed in the request.'}), 400
            response = random_verb(data)
            return response
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
        except Exception:
            return jsonify({'error': 'Something happened when requesting a verb'}), 500

    except Exception:
        return jsonify({'error': 'Something happened when trying to request a verb'}), 500


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