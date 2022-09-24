from scorecard import Scorecard

class Player:
    def __init__(self, gap: int, id: str):
        self.gap = gap
        self.scorecard = Scorecard()
        self.id = id

    def update_gap(self, new_gap: int):
        self.gap = new_gap
