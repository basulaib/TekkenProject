from flask import render_template, flash, redirect, url_for, request, g, jsonify, current_app
from app import db
from app.models import Character, CharacterMove
from app.main import bp
from app.tables import MoveTable, CharacterTable
from datetime import datetime
import os

def last_updated(folder):
    """
    https://stackoverflow.com/a/54164514
    """
    return str(max(os.path.getmtime(os.path.join(root_path, f))
                   for root_path, dirs, files in os.walk(folder)
                   for f in files))

@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index/', methods=['GET', 'POST'])
def index():
    #moves = CharacterMove.query.filter_by(character='negan').all()
    #table = MoveTable(moves)
    #table.border = True
    #return render_template('index.html', title='Test', table=table, last_updated=last_updated('app/static/js'))