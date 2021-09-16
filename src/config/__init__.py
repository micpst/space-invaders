import os
import json

class Settings:
    
    _instance = None
    _path = os.path.join(os.path.dirname(__file__), 'settings.json')
    
    def __new__(cls):
        if cls._instance is None:
            # Create the only instance of cls:
            self = super(Settings, cls).__new__(cls)
            cls._instance = self

            # Set the defaults:
            cls.__init__(self)
            cls.__init__ = lambda s: None

            # Load the current config from disk:
            self.load()

        return cls._instance

    def __init__(self):
        self.difficulty = 'normal'
        self.player_color = 'yellow'
        self.player_name = 'Player #1'

    def load(self):
        with open(self._path, 'r') as f:
            self.__dict__.update(json.load(f))

        return self

    def save(self):
        with open(self._path, 'w') as f:
            json.dump(self.__dict__, f, indent=4)

SETTINGS = Settings()