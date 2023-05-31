numbers = open("input").read().strip("\n").split(" ")
numbers = [int(nb) for nb in numbers]


def parse_node(numbers):
    nb_subnodes, nb_entries = numbers[0], numbers[1]
    subnodes = []
    entries = []
    length = 0
    for _ in range(nb_subnodes):
        subnode, sub_length = parse_node(numbers[2 + length :])
        length += sub_length
        subnodes.append(subnode)
    entries = numbers[2 + length : 2 + length + nb_entries]
    length += 2 + nb_entries
    return (subnodes, entries), length


def sum_metadata(tree):
    total = 0
    for subnode in tree[0]:
        total += sum_metadata(subnode)
    total += sum(tree[1])
    return total


def indexed_sum_metadata(tree):
    total = 0
    if len(tree[0]) == 0:
        total += sum(tree[1])
    for i, subnode in enumerate(tree[0]):
        weight = tree[1].count(i + 1)
        total += weight * indexed_sum_metadata(subnode)
    return total


tree, _ = parse_node(numbers)

print(indexed_sum_metadata(tree))
