from flask import Blueprint, current_app, render_template, request, Response, session

bp = Blueprint('template', __name__, url_prefix='/')

@bp.route('')
def index():
    return render_template('home/home.html', title='Base')

@bp.route('/home')
def home():
    return render_template('home/home.html', title='Calculadora - Home')

@bp.route('/sobre')
def sobre():
    return render_template('sobre/sobre.html', title='Calculadora - Sobre')

@bp.route('/hist')
def historico():
    return render_template('historico/historico.html', title='Calculadora - Histórico')
