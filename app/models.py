from datetime import datetime
import json
import os
from flask import current_app, url_for
from app import db
from flask_sqlalchemy import DeclarativeMeta

class Character(db.Model):
    __tablename__ = 'characters'
    char_id = db.Column(db.Integer, primary_key=True, index=True, unique=True)
    name = db.Column(db.String(32), index=True, unique=True, nullable=False)
    moves = db.relationship('CharacterMove', backref='owner', lazy=True)
    def __repr__(self):
        return '<Character: {}>'.format(self.name)
    
class CharacterMove(db.Model):
    __tablename__ = 'character_moves'
    move_id = db.Column(db.Integer, primary_key=True)
    character = db.Column(db.String(32), db.ForeignKey('characters.name'))
    command = db.Column(db.String(128), default="''", nullable=False)
    hit_level = db.Column(db.String(64))
    damage = db.Column(db.String(64))
    start_frame = db.Column(db.String(64))
    block_frame = db.Column(db.String(64))
    hit_frame = db.Column(db.String(64))
    counter_hit_frame = db.Column(db.String(64))
    notes = db.Column(db.String(64))
    
    def __repr__(self):
        return (
            f"Character: {self.character}\n"
            f"Move ID: {self.move_id}\n"
            f"Command: {self.command}\n"
            f"Hit level: {self.hit_level}\n"
            f"Damage: {self.damage}\n"
            f"Start frame: {self.start_frame}\n"
            f"Block frame: {self.block_frame}\n"
            f"Hit frame: {self.hit_frame}\n"
            f"Counter hit frame: {self.counter_hit_frame}\n"
            f"Notes: {self.notes}"
        )