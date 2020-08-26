# coding: utf-8
from sqlalchemy import Column, ForeignKey, Integer, String, text
from sqlalchemy.dialects.mysql import VARCHAR
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Character(Base):
    __tablename__ = 'characters'
    __table_args__ = {'comment': 'A table for characters names'}

    char_id = Column(Integer, primary_key=True, unique=True, server_default=text("'0'"))
    name = Column(String(32), nullable=False, unique=True)


class CharacterMove(Base):
    __tablename__ = 'character_moves'
    __table_args__ = {'comment': 'A table for the moves of the characters of TEKKEN 7'}

    move_id = Column(Integer, primary_key=True)
    character = Column(ForeignKey('characters.name'), nullable=False, index=True)
    command = Column(VARCHAR(128), nullable=False, server_default=text("''"))
    hit_level = Column(VARCHAR(64))
    damage = Column(VARCHAR(64))
    start_frame = Column(VARCHAR(64))
    block_frame = Column(VARCHAR(64))
    hit_frame = Column(VARCHAR(64))
    counter_hit_frame = Column(VARCHAR(64))
    notes = Column(VARCHAR(64))

    character1 = relationship('Character')
