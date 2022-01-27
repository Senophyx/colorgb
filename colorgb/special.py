# BETA!








import random
import os
import platform
from time import sleep

class clear:
    def __init__(self, delay:int=None):
        if platform.uname()[0] == "Windows":
            if delay == None:
                pass
            else:
                sleep(delay)
            os.system("cls")
            
        else:
            if delay == None:
                pass
            else:
                sleep(delay)
            os.system("clear")

color_list = [
    '\033[31m',
    '\033[32m',
    '\033[33m',
    '\033[34m',
    '\033[35m',
    '\033[36m',
    '\033[37m'
]

def blink(text, loop=20) -> str:
    for i in range(loop):
        random_color = random.choice(color_list)
        clear(delay=0.1)
        colored = f"{random_color}{text}\033[0m"
        print(colored)
