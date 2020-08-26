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
        return 'Character: {}\n Move: {}\n Command: {}\n Hit Level: {}\n Damage: {}\n Start Frame: {}\n Block Frame: {}\n Hit Frame: {}\n CH Frame: {}\n Notes: {}'.format(self.character,self.move_id,self.command,self.hit_level,self.damage,self.start_frame,self.block_frame,self.hit_frame,self.counter_hit_frame,self.notes)
    