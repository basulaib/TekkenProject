from flask_table import Table, Col

class CharacterTable(Table):
    char_id = Col('Character ID', show=False)
    name = Col('Character name')
    moves = Col('Character moves')

class MoveTable(Table):
    move_id = Col('Move ID', show=False)
    character = Col('Character', show=False)
    command = Col('Command')
    hit_level = Col('Hit level')
    damage = Col('Damage')
    start_frame = Col('Start frame')
    block_frame = Col('Block frame')
    hit_frame = Col('Hit frame')
    counter_hit_frame = Col('Counter hit frame')
    notes = Col('Notes')