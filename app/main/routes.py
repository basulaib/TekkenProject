from flask import render_template, flash, redirect, url_for, request, g, jsonify, current_app
from app import db
from app.models import Character, CharacterMove
from app.main import bp
from datetime import datetime

@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index/', methods=['GET', 'POST'])
def index():
    t = str(datetime.now())
    return render_template('index.html', title='Test', time=t)