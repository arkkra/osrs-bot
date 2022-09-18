from .base import BaseScript
from utils import Sleep, click, random_sleep

class HighAlch(BaseScript):
    def pre(self):
        pass

    def post(self):
        pass

    def stop_pressed(self):
        if self.stop():
            print('bro we stopped yo')

    def do(self):
        while True and not self.stop():
            click()
            random_sleep(Sleep(time=1.33, delay=.36))

