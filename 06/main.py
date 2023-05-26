from collections import defaultdict
from typing import List

MAX_DIST = 10000

file = open("input").read().split("\n")[:-1]
coordinates = [tuple(int(num) for num in line.split(", ")) for line in file]
print(coordinates)


def manhattan_distance(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])


def find_closest_point(target: tuple, points: List[tuple]):
    min_distance = 500
    closest_point = points[0]
    tied = False
    for point in points:
        dist = manhattan_distance(point, target)
        if dist == min_distance:
            tied = True
        if dist < min_distance:
            min_distance = dist
            closest_point = point
            tied = False
    return (closest_point, tied)


def is_close(target: tuple, points: List[tuple]):
    total_dist = 0
    for point in points:
        dist = manhattan_distance(point, target)
        total_dist += dist
        if total_dist >= MAX_DIST:
            return False
    return True


print("Part 1:")

infinite = set()
areas = defaultdict(int)

for x in range(400):
    for y in range(400):
        closest_point, tied = find_closest_point((x, y), coordinates)
        if tied:
            continue
        if closest_point in infinite:
            continue
        if x == 0 or x == 399 or y == 0 or y == 399:
            infinite.add(closest_point)
            areas[closest_point] = 0
        else:
            areas[closest_point] += 1


print(f"areas : {areas}")

print(f"infinite : {infinite}")

biggest_area = max(areas.values())

print(biggest_area)

print("Part 2:")

close_points = sum(
    is_close((x, y), coordinates) for x in range(400) for y in range(400)
)

print(f"Answer : {close_points}")
