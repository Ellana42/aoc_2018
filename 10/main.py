import re
from time import sleep

import numpy as np

SCREEN = (200, 300)

coordinates = open("input").read().split("\n")[:-1]
coordinates = [
    [int(x) for x in re.findall(r"-*\d+", coordinate)] for coordinate in coordinates
]
coordinates = [(np.array(x[:2]), np.array(x[2:])) for x in coordinates]
position, velocity = zip(*coordinates)
position, velocity = np.array(position), np.array(velocity)
print(position)
print(velocity)


def plot_coordinates(position):
    for y in range(SCREEN[0]):
        for x in range(SCREEN[1]):
            is_in_list = np.any(np.all(np.array([x, y]) == position, axis=1))
            if is_in_list:
                print(u"\u2588", end="")
            else:
                print(" ", end="")
        print()


close = False
time = 0
while True:
    position += velocity
    time += 1
    if not close and np.linalg.norm(position) < 3500:
        close = True
    if close:
        plot_coordinates(position)
        print(time)
        sleep(0.3)
