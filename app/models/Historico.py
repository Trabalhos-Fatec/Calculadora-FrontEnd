from app import db
from datetime import datetime
import json

class Historico(db.Model):

    __tablename__= 'historico'
    id_historico = db.Column(db.Integer, primary_key=True)
    argumento = db.Column(db.String, nullable=False)
    resultado = db.Column(db.String, nullable=False)
    dt_registro = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, argumento, resultado):
        self.argumento = argumento
        self.resultado = resultado


    def __repr__(self):
        return json.dumps({ 
            'id_historico': self.id_historico, 
            'argumento': self.argumento, 
            'resultado': self.resultado, 
            'dt_registro': self.dt_registro 
            })
        
    