file = open("input").read()
numbers = file.split("\n")[:-1]
numbers = [eval(number) for number in numbers]
result = sum(numbers)
print(result)
