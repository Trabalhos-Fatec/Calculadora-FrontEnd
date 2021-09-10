from flask.blueprints import Blueprint
from app import db
from Flask import Blueprint, request, jsonify, current_app

bp = Blueprint('operacao', __name__, url_prefix='/operacao')

