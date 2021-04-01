class MenuModel:
    def __init__(self):
        self.options = [
            'Play', 
            'Settings', 
            'Quit',
        ]
        self.input_tick = 0
        self.index = 0