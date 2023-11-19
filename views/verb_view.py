import requests
from flask import Blueprint, request, jsonify
import json
from helpers.token_validation import validate_token

verb = Blueprint("verb", __name__)

# ENDPOINT 1 - GET A SINGLE VERB
@verb.route("/verbs/", methods=["GET"])
def get_single_verb():
    pass

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