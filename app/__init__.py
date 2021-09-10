from flask import Flask, render_template, session
# from flask_sqlalchemy import SQLAlchemy
import os

# Settings
template_dir = os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
template_dir = os.path.join(template_dir, 'app')
template_dir = os.path.join(template_dir, 'views')
app = Flask(__name__, template_folder=template_dir, static_folder=template_dir)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:fatec@127.0.0.1:33006/calculadoradb'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)


