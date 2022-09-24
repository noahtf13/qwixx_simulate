import numpy as np


class Dice:
    def __init__(self):
        self.dice = list()
        name_list = ['white_1', 'white_2', 'red', 'yellow', 'green', 'blue']
        for die in name_list:
            if die in ['white_1', 'white_2']:
                self.dice.append({
                    'name': die,
                    'color': 'white',
                    'value': None
                })
            else:
                self.dice.append({
                    'name': die,
                    'color': die,
                    'value': None
                })

    def roll(self, white_only: bool = False):
        new_dice = self.dice.copy()
        if white_only:
            for die in new_dice:
                if die['color'] == 'white':
                    die['value'] = np.random.randint(1, 7)
        else:
            for die in new_dice:
                die['value'] = np.random.randint(1, 7)
        self.dice = new_dice

    def remove_die(self, color: str):
        keep_dice = [i for i in self.dice if i['color'] != color]
        self.dice = keep_dice

    def possible_moves(self, whites = False):
        possible_moves = list()
        white_list = list()
        white_sum = 0
        if whites:
            for die in self.dice:
                if die['color'] == 'white':
                    white_sum += die['value']
                    white_list.append(die['value'])
            for color in ['red', 'yellow', 'green', 'blue']:
                possible_moves.append({
                    'color': color,
                    'number': white_sum,
                    'whites': True
                })
        else:
            for die in self.dice:
                if die['color'] == 'white':
                    white_sum += die['value']
                    white_list.append(die['value'])
                else:
                    for white_value in white_list:
                        possible_moves.append({
                            'color': die['color'],
                            'number': die['value'] + white_value,
                            'whites': False
                        })

        return possible_moves












