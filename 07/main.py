import string

# list of unlocked steps -> remove related instructions
# each pass 1. add newly unlocked steps to list 2. select first alphabetical unlocked step
# step -> add related steps to unlocked

# Maybe just remove instructions that are irrelevant and add element if in no more instructions

file = open("input").read().split("\n")[:-1]

instructions = set((line.split(" ")[1], line.split(" ")[7]) for line in file)
undone_steps = set(string.ascii_uppercase)
unlocked_steps = undone_steps - {el[1] for el in instructions}

done_steps = []

while undone_steps:
    next_step = min(unlocked_steps)
    done_steps.append(next_step)
    undone_steps.discard(next_step)
    unlocked_steps.discard(next_step)
    instructions = set(el for el in instructions if el[0] != next_step)
    unlocked_steps |= undone_steps - {el[1] for el in instructions}

print("".join(done_steps))
