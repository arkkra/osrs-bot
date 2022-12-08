from .base import BaseScript
from utils import Sleep, RepeatTimer, click, random_sleep


class Clicker(BaseScript):
    def __init__(self):
        super().__init__()
        self.knight_timer = RepeatTimer(60, click, delay=30, immediate_first=True)

    def pre(self):
        pass

    def post(self):
        pass
    
    def stop_pressed(self):
        print('is this even getting called')
        if self.stop:
            print('wtf')
            self.knight_timer.cancel()
        else:
            self.knight_timer = RepeatTimer(60, click, delay=30, immediate_first=True)
            self.knight_timer.start()

    def do(self):
        self.knight_timer.start()
        self.listener.join()
