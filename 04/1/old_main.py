from enum import Enum

Event = Enum("Event", ["SHIFT", "ASLEEP", "WAKE"])


def get_timestamp(entry):
    timestamp = (
        entry.split("]")[0]
        .strip("[")
        .replace(" ", "")
        .replace("-", "")
        .replace(":", "")
    )
    return int(timestamp)


def parse_entry(entry):
    guard = -1
    timestamp = get_timestamp(entry)
    infos = entry.split("]")[1]
    if infos == " falls asleep":
        event = Event("ASLEEP")
    elif infos == " wakes up":
        event = Event("WAKE")
    else:
        event = Event("SHIFT")
        guard = infos.split(" ")[2].strip("#")
    return (timestamp, event, guard)


guards = {}

entries = open("input").read().split("\n")[:10]
entries.sort(key=get_timestamp)
current_guard = -1
last_time_asleep = 0

for entry in entries:
    timestamp, event, guard = parse_entry(entry)
    if guard != -1:
        current_guard = guard

    if event == Event("ASLEEP"):
        last_time_asleep = timestamp
