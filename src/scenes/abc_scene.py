from abc import ABCMeta, abstractmethod

class GameScene(metaclass=ABCMeta):
    @abstractmethod
    def on_enter(self):
        pass
    
    @abstractmethod
    def on_exit(self):
        pass

    @abstractmethod
    def on_event(self, ev):
        pass

    @abstractmethod
    def update(self, time_ms):
        pass

    def draw(self, screen):
        for key in self.__dict__:
            self.__dict__[key].draw(screen)