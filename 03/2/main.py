def parse_claim(claim):
    claim = claim.split(" ")[2:]
    x, y = claim[0].strip(":").split(",")
    h, w = claim[1].split("x")
    return (int(x), int(y), int(h), int(w))

def range_to_coordinates(x, y, width, height):
    return {(a + x, b + y) for a in range(width) for b in range(height)}

file = open("input").read().split("\n")[:-1]

spots_taken = set()
spots_contested = set()
claims = []

for line in file:
    claim_coordinates = parse_claim(line)
    coordinates = range_to_coordinates(*claim_coordinates)
    claims.append(coordinates)
    spots_contested.update(spots_taken.intersection(coordinates))
    spots_taken.update(coordinates)

for index, claim in enumerate(claims):
    if not claim.intersection(spots_contested) :
        print(index + 1)
        break
