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
    return datetime.strptime(timestamp, FORMAT), action, int(guard)


entries = open("input").read().split("\n")[:-1]
entries = [parse_entry(entry) for entry in entries]
entries.sort(key=lambda e: e[0].time())
print(entries)
entries.sort(key=lambda e: e[0])
current_guard = -1

guards = defaultdict(list)
fell_asleep = entries[0][0]

for entry in entries:
    match entry[1]:
        case "G":
            current_guard = entry[2]
        case "F":
            fell_asleep = entry[0]
        case "W":
            guards[current_guard].append((fell_asleep, entry[0]))

sleep_times = { guard: sum((stop - start for (start, stop) in sleeping), timedelta()).total_seconds() / 60 for guard, sleeping in guards.items() }
biggest_sleeper = max(sleep_times, key=lambda x : sleep_times[x])
print(biggest_sleeper)
print(sleep_times[biggest_sleeper])
# for guard, sleeping in guards.items() :
#     for (start, stop) in sleeping:
#         print(stop - start)
