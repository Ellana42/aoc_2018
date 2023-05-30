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

print("Answer 1")
# print("".join(done_steps))

print("Part 2 " + 10 * "-")


def get_timing(letter):
    return ord(letter) - 4


instructions = set((line.split(" ")[1], line.split(" ")[7]) for line in file)
undone_steps = set(string.ascii_uppercase)
unlocked_steps = undone_steps - {el[1] for el in instructions}

done_steps = []
total_time = 0
workers = 2
doing = {}

next_step = None

while undone_steps:

    print("-" * 20 + "seconde " + str(total_time))
    # Assign to next step
    while workers and unlocked_steps:
        element = min(unlocked_steps)
        workers -= 1
        doing[element] = get_timing(element)
        unlocked_steps.discard(element)

    print(f"workers {workers}")
    print(f"doing {doing}")

    # Increase time
    total_time += 1
    doing = {task: time - 1 for task, time in doing.items() if time > 0}

    # Check if done
    done = set(el for el, time in doing.items() if time == 0)
    print(f"done {done}")
    workers += len(done)
    done_steps.extend(list(done))  # Multiple things at the same time
    print(f"done_steps {done_steps}")

    # Update lists
    doing = {key: value for key, value in doing.items() if key not in done}
    undone_steps -= done
    print(f"undone_steps {undone_steps}")
    instructions = set(el for el in instructions if el[0] not in done)
    print(f"instructions {instructions}")
    unlocked_steps |= undone_steps - {el[1] for el in instructions}
    unlocked_steps -= set(doing.keys())
    print(f"unlocked_steps {unlocked_steps}")

print("".join(done_steps))
print(total_time)
