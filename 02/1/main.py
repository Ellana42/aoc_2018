from collections import Counter

two_times = 0
three_times = 0
file = open("input").read().split("\n")
for line in file:
    counter = Counter(line)
    if 2 in counter.values():
        two_times += 1
    if 3 in counter.values():
        three_times += 1

print(two_times * three_times)
