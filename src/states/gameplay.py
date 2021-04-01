import pygame

from .game import GameState

class GameplayState(GameState):
	def __init__(self, game, game_over_state):
		super().__init__(game)
		self.game_over_state = game_over_state
		self.swarm_speed = 500

		self.player_controller = PlayerController(0, 540)
		self.swarm_controller = SwarmController(800, 48, self.swarm_speed)
		self.explosion_controller = ExplosionController(self.game)
		self.collision_controller = CollisionController(self.game, self.swarm_controller, self.player_controller, self.explosion_controller, self)

		self.controllers = [ 
            self.swarm_controller, 
            self.player_controller, 
            self.collision_controller, 
            self.explosion_controller 
        ]

		self.views = [ 
            PlayerView(self.player_controller, 'ship.png'), 
            InvaderView(self.swarm_controller, 'invaders.png'), 
            PlayerLivesView(self.player_controller, 'ship.png'), 
            BulletView(self.player_controller.bullets, 'bullet.png'), 
            BulletView(self.swarm_controller.bullets, 'alienbullet.png'), 
            ExplosionView(self.explosion_controller.list.explosions, 'explosion.png', 32, 32)
        ]
		
	def on_enter(self):
		self.player_controller.pause(False)
		
	def update(self, game_time):
		for controler in self.controllers:
			controler.update(game_time)	
			
		if self.player_controller.model.lives == 0:
			self.game.change_state(self.game_over_state)
			
		if len(self.swarm_controller.invaders) == 0:
			self.swarm_speed -= 50
			if self.swarm_speed < 100:
				self.swarm_speed = 100
			
			self.swarm_controller.reset(48, self.swarm_speed)
			levelUpMessage = InterstitialState(self.game, 'Congratulations! Level Up!', 2000, self)
			self.game.changeState(levelUpMessage)