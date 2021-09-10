from app import db
from flask import Blueprint, request, jsonify, current_app
from app.models.Historico import Historico

bp = Blueprint('hist', __name__, url_prefix='/hist')


@bp.route('/save', methods=['POST'])
def saveHistorico():
    try:
        hist = Historico(argumento=request.json['argumento'], resultado=request.json['resultado'])
        db.session.add(hist)
        db.session.commit()

        return jsonify({"id_historico": hist.id_historico, "status": "salvo com sucesso"})

    except Exception as error:
        res = {'error': str(error)}
        return jsonify(res), 500