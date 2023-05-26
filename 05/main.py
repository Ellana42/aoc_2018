import string

file = open("input").read()[:-1]
print(file)


def is_polarised(letter1: str, letter2: str):
    if letter1.lower() != letter2.lower():
        return False
    if letter1.islower() and letter2.isupper():
        return True
    if letter1.isupper() and letter2.islower():
        return True
    return False


def remove_polymer(file: str, letter: str):
    file = file.replace(letter.lower(), "")
    file = file.replace(letter.upper(), "")
    return file


def reduce_polymer(file):
    result = []
    for letter in file:
        if len(result) > 0 and is_polarised(result[-1], letter):
            result.pop()
        else:
            result.append(letter)
    return result


result = reduce_polymer(file)
print("".join(result))
print(f"Answer 1: {len(result)}")

best_letter, size = "a", len(file)

for letter in string.ascii_lowercase:
    reduced_file = remove_polymer(file, letter)
    reduced_file = reduce_polymer(reduced_file)
    if len(reduced_file) < size:
        best_letter, size = letter, len(reduced_file)

print(f"Best letter : {best_letter}")
print(f"Answer 2: {size}")
