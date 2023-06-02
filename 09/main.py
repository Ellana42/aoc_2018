import re

file = open("test").read().split("\n")[0]
nb_players, last_marble = tuple(int(nb) for nb in re.findall(r"\d+", file))


def get_next_position(current_position, lenght_circle):
    new_position = current_position + 2
    if new_position <= lenght_circle:
        return new_position
    else:
        return new_position % lenght_circle


circle = [0, 1]
next_marble = 2
current_player = 2
position_current = 1
players = [0 for _ in range(nb_players)]
print(players)

while next_marble <= last_marble:
    if next_marble % 23 == 0:
        print("23 process : ")
        players[current_player] += next_marble
        print(next_marble)
        players[current_player] += circle.pop(-7)
        current_position = len(circle) - 7
        print(current_position)
        print(circle[current_position])
    position_current = get_next_position(position_current, len(circle))
    circle.insert(position_current, next_marble)
    next_marble += 1
    current_player = current_player + 1 % nb_players
