from collections import defaultdict
from datetime import datetime, timedelta
import re

FORMAT = "[%Y-%m-%d %H:%M]"
reg = re.compile(r".*#(\d*).*")


def parse_entry(entry: str):
    timestamp, info = entry[:18], entry[19:]
    guard = re.search(reg, info)
    guard = guard.group(1) if guard else -1
    action = info[0].upper()
    return datetime.strptime(timestamp, FORMAT), action, guard


entries = open("input").read().split("\n")[:-1]
entries = [parse_entry(entry) for entry in entries]
entries.sort(key=lambda e: e[0])
current_guard = -1

guards = defaultdict(lambda : timedelta(minutes=0))
last_time_asleep = entries[0][0]

for entry in entries:
    match entry[1]:
        case "G":
            current_guard = entry[2]
        case "F":
            last_time_asleep = entry[0]
        case "W":
            guards[current_guard] += entry[0] - last_time_asleep

# print(guards)
biggest_sleeper = max(guards, key=lambda x : guards[x].total_seconds())
print(int(biggest_sleeper) * int(guards[biggest_sleeper].total_seconds() / 60))
