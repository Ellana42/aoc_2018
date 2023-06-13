import numpy as np

serial_number = int(open("input").read())

SIZE_GRID = 300
X, Y = 101, 153
SN = 4151


def get_power_level(x, y, serial_number):
    rack_id = x + 10
    start_power_level = rack_id * y
    power_level = (start_power_level + serial_number) * rack_id
    hundreds_digit = (power_level // 100) % 10
    return hundreds_digit - 5


def cell_get(grid, x=X, y=Y):
    return grid[y - 1][x - 1]


x1 = list(range(1, SIZE_GRID + 1))
y1 = list(range(1, SIZE_GRID + 1))
x, y = np.meshgrid(x1, y1)
grid = get_power_level(x, y, SN)

max_sum = 0
max_x, max_y, max_s = 0, 0, 0

for s in range(SIZE_GRID):
    for x in range(SIZE_GRID - s):
        for y in range(SIZE_GRID - s):
            su = np.sum(grid[y : y + s, x : x + s])
            if su > max_sum:
                max_x, max_y, max_s = x, y, s
                max_sum = su

print(f"max sum = {max_sum}")
print(f"coordinates : ({max_x + 1}, {max_y + 1}, {max_s})")
