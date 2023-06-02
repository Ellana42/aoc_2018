import re

file = open("input").read()
nb_players, last_marble = tuple(int(nb) for nb in re.findall(r"\d+", file))


def get_position(current_position, lenght_circle, i):
    new_position = current_position + i
    if 0 <= new_position <= lenght_circle:
        return new_position
    else:
        return new_position % lenght_circle


circle = [0, 1]
next_marble = 2
current_player = 2
position_current = 1
players = [0 for _ in range(nb_players)]

while next_marble <= last_marble:
    lenght_circle = len(circle)
    if next_marble % 23 == 0:
        players[current_player] += next_marble
        marble_to_remove = get_position(position_current, lenght_circle, -7)
        players[current_player] += circle.pop(marble_to_remove)
        position_current = get_position(marble_to_remove, lenght_circle, 0)
    else:
        position_current = get_position(position_current, lenght_circle, 2)
        circle.insert(position_current, next_marble)
    next_marble += 1
    current_player = (current_player + 1) % nb_players

print(max(players))
