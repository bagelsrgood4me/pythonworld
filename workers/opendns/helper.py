import time
import random


def sum(x, y):
    sleep_timer = random.randint(0, 3)
    time.sleep(sleep_timer)
    return x + y