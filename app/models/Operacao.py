from app import db
from app.models.Historico import Historico
import json

class Operacao(db.Model):
    __tablename__= 'operacao'
    id_operacao = db.Column(db.Integer, primary_key=True)
    tipo_operacao = db.Column(db.String, nullable=False)
    operacao_especifica = db.Column(db.String, nullable=False)
    resultado = db.Column(db.String, nullable=False)
    id_historico = db.Column(db.Integer, db.ForeignKey('Historico.id_historico'), nullable=False)

    def __init__(self, id_operacao, tipo_operacao, operacao_especifica, resultado, id_historico):
        self.id_operacao = id_operacao
        self.tipo_operacao = tipo_operacao
        self.operacao_especifica = operacao_especifica
        self.resultado = resultado
        self.id_historico = id_historico


    def __repr__(self):
        return json.dumps({ 
            'id_operacao': self.id_operacao, 
            'tipo_operacao': self.tipo_operacao, 
            'operacao_especifica': self.operacao_especifica,
            'resultado': self.resultado,
            'id_historico': self.id_historico
        })