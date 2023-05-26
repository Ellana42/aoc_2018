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


result = []

for letter in file:
    if len(result) > 0 and is_polarised(result[-1], letter):
        result.pop()
    else:
        result.append(letter)

print("".join(result))
print(f"Answer 1: {len(result)}")
