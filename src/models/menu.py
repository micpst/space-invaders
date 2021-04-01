class MenuModel:
    def __init__(self):
        self.index = 0
        self.timeout = 0
        self.options = ['Play', 'Settings', 'Quit']

    def tick(self):
        self.timeout= 150

    def update(self, time):
        self.timeout = max(0, self.timeout - time)

    def move(self, direction):
        if direction == 'up':
            self.index -= 1
            if self.index < 0:
                self.index = len(self.options) - 1

        elif direction == 'down':
            self.index += 1
            if self.index == len(self.options):
                self.index = 0

        else:
            raise ValueError('Unsupported direction!')