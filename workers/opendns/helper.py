import time
import random


def sum(x, y):
    sleep_timer = random.randint(0, 60)
    print(sleep_timer)
    time.sleep(sleep_timer)
    return x + y