from .base import BaseScript
from libs.libs import click, random_sleep
from models.models import Sleep

class HighAlch(BaseScript):

    def position(self):
        pass

    def do(self):
        click()
        random_sleep(Sleep(time=1.33, delay=.36))
        # mouse.press(Button.left)
        # randomTime = random.randint(9, 27)
        # time.sleep(randomTime / 100)
        # mouse.release(Button.left)
        # randomTime = random.randint(133, 166)
        # time.sleep(randomTime / 100)

