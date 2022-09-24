class Scorecard:
    def __init__(self):
        self.rows = dict()
        self.max_x = dict()
        self.skipped_turns = 0
        self.colors = ['red', 'yellow', 'green', 'blue']
        for color in self.colors:
            self.rows[color] = dict()
            self.max_x[color] = 0
            for num in range(2, 13):
                self.rows[color][num] = False

    def add_x(self, color, number):
        self.rows[color][number] = True
        for color, numbers in self.rows.items():
            if color in ['red', 'yellow']:
                max_num = 0
                for number, state in numbers.items():
                    if state is True and number > max_num:
                        max_num = number
                self.max_x[color] = max_num
            else:
                max_num = 13
                for number, state in numbers.items():
                    if state is True and number < max_num:
                        max_num = number
                self.max_x[color] = max_num

    def close_eligibility(self):
        eligibility = {}
        for color, info in self.rows.items():
            num_crossed = 0
            print(1)
            for number, crossed in self.rows[color].items():
                if crossed:
                    num_crossed = num_crossed + 1
            if num_crossed >= 5:
                eligibility[color] = True
            else: 
                eligibility[color] = False
 

        return eligibility



    def missed_turn(self):
        self.skipped_turns += 1
