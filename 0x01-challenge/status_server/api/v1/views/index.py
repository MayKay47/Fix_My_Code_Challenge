#!/usr/bin/python3
# in api.v1.views module

from flask import Blueprint, jsonify

app_views = Blueprint('app_views', __name__)


@app_views.route('/status', methods=['GET'])
def status():
    return jsonify({"status": "OK"})
