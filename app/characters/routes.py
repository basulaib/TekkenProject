from flask import render_template, flash, redirect, url_for, request, g, jsonify, current_app
from app import db
from app.main.routes import last_updated
from app.models import Character, CharacterMove
from app.characters import bp
from app.tables import MoveTable, CharacterTable
from datetime import datetime

@bp.route('/characters')
def characters():
    chars = Character.query.all()
    table = CharacterTable(chars)
    return render_template('characters.html', table=table, last_updated=last_updated('app/static/js'))

@bp.route('/characters/<character>')
def char(character):
    """Routing for individual character page.

    Args:
        character (String): Character to be queried

    Returns:
        Character data page if found, else 404
    """
    c = Character.query.filter_by(name=character).first_or_404()
    moves = CharacterMove.query.filter_by(character=c.name).all()
    table = MoveTable(moves)
    return render_template('characters.html', table=table, last_updated=last_updated('app/static/js'))