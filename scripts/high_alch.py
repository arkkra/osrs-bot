from .base import BaseScript
from utils import Sleep, click, random_sleep

class HighAlch(BaseScript):
    def pre(self):
        pass

    def post(self):
        pass

    def do(self):
        while True:
            click()
            random_sleep(Sleep(time=1.33, delay=.36))

