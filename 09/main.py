from collections import deque
import re

file = open("input").read()
nb_players, last_marble = tuple(int(nb) for nb in re.findall(r"\d+", file))
last_marble *= 100

circle = deque()
next_marble = 0
current_player = 0
players = [0 for _ in range(nb_players)]

while next_marble <= last_marble:
    if next_marble > 0 and next_marble % 23 == 0:
        players[current_player] += next_marble
        circle.rotate(7)
        players[current_player] += circle.popleft()
    else:
        circle.rotate(-2)
        circle.appendleft(next_marble)
    next_marble += 1
    current_player = (current_player + 1) % nb_players

print(max(players))
