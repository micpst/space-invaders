from abc import ABC, abstractmethod

class GameState(ABC):
	@abstractmethod
	def on_enter(self):
		pass
	
	@abstractmethod
	def on_exit(self):
		pass
	
	@abstractmethod
	def update(self, game_time):
		pass

	@abstractmethod
	def draw(self, window):
		pass