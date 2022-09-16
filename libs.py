import mouse
import random
import time

from models import Sleep

def random_sleep(sleep: Sleep):
    if sleep.time:
        rand = random.uniform(0, sleep.delay)
        time.sleep(sleep.time + rand)

def move(x: int, y: int)

def click(sleep: Sleep=Sleep()):
    mouse.click()
    random_sleep(sleep)
    mouse.release()

def get_random_coordinate_within_box(x: int, y: int, dx: int, dy: int):
    xx = random.randrange(dx)
    yy = random.randrange(dy)
    return x + xx, y + yy
