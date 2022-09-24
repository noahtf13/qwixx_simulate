from dice import Dice
from player import Player
import numpy as np


class Game:
    def __init__(self, players: list[Player]):
        self.players = players
        self.turn = np.random.randint(1, len(players)+1)
        self.dice = Dice()
        self.game_colors = ['red', 'yellow', 'green', 'blue']
        new_players = []
        i = 1
        for player in self.players:
            new_players.append(
                Player(gap=player['gap'], id=i, name=player['name'])
            )
            i=i+1
        self.players = new_players

    def _get_gaps(self, possible_moves: list[dict], player: Player):
        gaps = dict()
        for color in player.scorecard.colors:
            max_of_color = [i for i in player.scorecard.max_x if i['color'] == color]
            relevant_moves = [i for i in possible_moves if i['color'] == color]
            for move in relevant_moves:
                if move['value'] > max_of_color:
                    gaps['color'] = color
                    gaps['value'] = move['value'] - max_of_color
                    gaps['move'] = move['value']
                    gaps['whites'] = move['whites']

        return gaps

    # def turn(self):
    #     self.dice.roll()
    #     acceptable_move = []
    #     for player in self.players:
    #         gaps = self._get_gaps(self.dice.possible_moves(whites=True), player)
    #         for gap in gaps:
    #             if gap['value'] <= player.gap:
    #                 acceptable_move.append(gap['move'])
            

    #     for player in self.players:
    #         gaps = self._get_gaps(self.dice.possible_moves(), player)
    #         if player.id == self.turn:
                
    #         else:
    #             for gap in [gap for gap in gaps if gap['whites'] is True]:
    #                 if gap['value'] <= player.gap:
    #                     acceptable_move.append(gap['move'])                     
    #     for move in acceptable_move:
            


    #     self.turn += 1

