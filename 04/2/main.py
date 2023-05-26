# Hours go from 23h45 to 0h59 -> 75 slots
from collections import defaultdict
import re
reg = re.compile(r".*#(\d*).*")


def get_timestamp(entry):
    timestamp = (
        entry.split("]")[0]
        .strip("[")
        .replace(" ", "")
        .replace("-", "")
        .replace(":", "")
    )
    return int(timestamp)

def parse_entry(entry: str):
    info = entry[19:]
    guard = re.search(reg, info)
    guard = guard.group(1) if guard else -1
    action = info[0].upper()
    return get_timestamp(entry) % 10000, action, int(guard)

def argmax(iterable):
    return max(enumerate(iterable), key=lambda x: x[1])

entries = open("input").read().split("\n")[:-1]
entries.sort(key=get_timestamp)
entries = [parse_entry(entry) for entry in entries]

guards = defaultdict(lambda : [0 for _ in range(75)])
current_guard = -1
fell_asleep = entries[0][0]

for entry in entries:
    match entry[1]:
        case "G":
            current_guard = entry[2]
        case "F":
            fell_asleep = entry[0]
        case "W":
            for i in range(fell_asleep, entry[0]):
                guards[current_guard][i] += 1

minute_most_asleep = {guard : argmax(guards[guard]) for guard in guards}
biggest_sleeper = max(minute_most_asleep, key=lambda x : minute_most_asleep[x][1])
print(f"biggest_sleeper {biggest_sleeper}")
print(f"minute_most_asleep {minute_most_asleep[biggest_sleeper][0]}")
print(f"answer {minute_most_asleep[biggest_sleeper][0] * biggest_sleeper}")
