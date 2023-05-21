from itertools import combinations


def differ_by_one(str1, str2, len_):
    differ = False
    diff_position = 0
    for i in range(len_):
        if str1[i] != str2[i] and not differ:
            differ = True
            diff_position = i
        elif str1[i] != str2[i] and differ:
            return False, diff_position
    return differ, diff_position


strings = open("input").read().split("\n")[:-1]
lenght_code = len(strings[0])
for pair in combinations(strings, 2):
    diff, position = differ_by_one(pair[0], pair[1], lenght_code)
    if diff:
        print(pair[0][:position] + pair[0][position + 1 :])
        break
