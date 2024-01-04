from itertools import combinations
def read_file():
    f = open("input.txt", "r")
    lines = f.readlines()
    f.close()
    return [int(line.rstrip('\n')) for line in lines]

def generate_combinations(input_list):
    all_combinations = []
    for r in range(1, len(input_list) + 1):
        all_combinations.extend(list(combinations(input_list, r)))
    return all_combinations

lines = read_file()
amount = 150
result = generate_combinations(lines)
# Part 1
count = 0
res = []
for i in result:
    if sum(i) == amount:
        count  = count + 1
        res.append(i)
print("Part 1: ",count)
# Part 2

l = []
for r in res:
    l.append(len(r))
print("Part 2: ",l.count(min(l)))