import math

from .base import BaseScript
from models import Sleep
from utils import get_random_coordinate_within_circle, move, \
    click, random_sleep, RepeatTimer

# AFK NMZ Range Script
# This assumes an inventory of 8 ranging potions, 19 absorbs, and 1 locator orb in that order
class RangeNMZ(BaseScript):
    def __init__(self):
        self.potion_cycle = Sleep(time=420, delay=60)
        self.locator_orb_cycle = Sleep(time=69, delay=30)
        self.potion_timer = RepeatTimer(420, self.click_potion, delay=60, immediate_first=True)
        self.locator_timer = RepeatTimer(69, self.click_locator, delay=30)
        self.potion_counter = 0

    def pre(self):
        random_sleep(sleep=Sleep(time=5))

    def post(self):
        pass 

    def click_locator(self):
        # hardcoded locator position bottom right. can do detection later
        x, y = get_random_coordinate_within_circle(1445, 840, 7)
        move(x, y)
        click()

        # double click in case hp gain has overlapped
        random_sleep()
        click()

    def click_potion(self):
        potion_number = int(math.floor(self.potion_counter / 4))
        if potion_number == 8:
            return
        if potion_number < 4:
             x, y = get_random_coordinate_within_circle(1326 + (potion_number * 42), 625, 6)
        else:
            x, y = get_random_coordinate_within_circle(1326 + ((potion_number - 4) * 42), 662, 6)

        move(x,y)
        click()
        self.potion_counter += 1

    def do(self):
        self.potion_timer.start()
        random_sleep(sleep=Sleep(time=1))
        self.locator_timer.start()
        
        
