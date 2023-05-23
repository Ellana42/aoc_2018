def get_timestamp(entry):
    timestamp = entry.split("]")[0].strip("[").replace(" ", "").replace("-", "").replace(":", "")
    return int(timestamp)

def parse_entry(entry):
    timestamp = get_timestamp(entry)


guards = {}

entries = open("input").read().split("\n")[:10]
entries.sort(key=get_timestamp)

for entry in entries:


