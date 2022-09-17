from .base import BaseScript
from libs import click, random_sleep
from models import Sleep

class HighAlch(BaseScript):
    def pre(self):
        pass

    def post(self):
        pass

    def do(self):
        while True:
            click()
            random_sleep(Sleep(time=1.33, delay=.36))

