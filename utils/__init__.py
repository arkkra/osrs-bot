import mouse
import random
import time
import math
from threading import Timer


class Sleep:
    def __init__(self, time=.2, delay=.3):
        self.time = time
        self.delay = delay


class RepeatTimer(Timer):
    def __init__(self, interval, function, delay=None, immediate_first=False, args=None, kwargs=None):
        super().__init__(interval, function, args=args, kwargs=kwargs)
        self.delay = delay
        self.immediate_first = immediate_first
        self.count = 0

    def run(self):
        while not self.finished.wait(0 if self.count == 0 and self.immediate_first \
                                     else self.interval + random.uniform(0, self.delay)):
            self.count += 1
            self.function(*self.args, **self.kwargs)


def random_sleep(sleep: Sleep=Sleep()):
    if sleep.time:
        rand = random.uniform(0, sleep.delay)
        time.sleep(sleep.time + rand)

def get_distance(x1: int, y1: int, x2: int, y2: int):
    if x1 == x2: 
        return math.abs(y1 - y2)
    elif y1 == y2:
        return math.abs(x1 - x2)
    return math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))

def move(x: int, y: int):
    # this sucks
    baseline = 150

    cur_x, cur_y = mouse.get_position()
    distance = get_distance(x, y, cur_x, cur_y)
    mouse.move(x, y, absolute=True, duration=(.04 * (distance/baseline)), steps_per_second=120.0)

def click():
    mouse.click()
    random_sleep()
    mouse.release()

def get_random_coordinate_within_box(x: int, y: int, dx: int, dy: int):
    xx = random.randrange(dx)
    yy = random.randrange(dy)
    return x + xx, y + yy

def get_random_coordinate_within_circle(x: int, y: int, radius: int):
    r = radius * math.sqrt(random.uniform(0, 1))
    theta = random.uniform(0, 1) * 2 * math.pi
    xx = x + r * math.cos(theta)
    yy = y + r * math.sin(theta)
    return xx, yy
