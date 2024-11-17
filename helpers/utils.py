import random
from time import sleep

def human_delay(min_delay=0.5, max_delay=2.0):
    sleep(random.uniform(min_delay, max_delay))
