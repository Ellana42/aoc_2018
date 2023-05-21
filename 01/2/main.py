file = open("input").read()
numbers = file.split("\n")[:-1]
numbers = [eval(number) for number in numbers]

result = 0
results = []

double = False
i = 0

while not double:
    # print(i)
    # i += 1
    for number in numbers:
        results.append(result)
        result += number
        if result in results:
            print(result)
            double = True
            break
