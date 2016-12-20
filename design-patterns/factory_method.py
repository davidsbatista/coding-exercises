class Cup(object):

    color = ''

    @staticmethod
    def get_cup(color):
        if color == 'red':
            return RedCup()
        elif color == 'green':
            return GreenCup()


class RedCup(Cup):
    def __init__(self):
        self.color = "red"


class GreenCup(Cup):
    def __init__(self):
        self.color = "green"