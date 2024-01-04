from itertools import permutations
def read_file():
    f = open("input.txt", "r")
    lines = f.readlines()
    f.close()
    return lines

def make_ingredient_dict(line):
    key, values = line.split(':')
    values = [int(val.split()[1]) for val in values.split(',')]
    my_dict = {"capacity": values[0], "durability": values[1], "flavor": values[2], "texture": values[3]}
    ingredients.append(my_dict)

def make_updated_ingredient_dict(line):
    key, values = line.split(':')
    values = [int(val.split()[1]) for val in values.split(',')]
    my_dict = {"capacity": values[0], "durability": values[1], "flavor": values[2], "texture": values[3],"calories":values[4]}
    ingredients.append(my_dict)

def generate_permutations(key_len):
    numbers = list(range(101))
    return [perm for perm in permutations(numbers, key_len) if sum(perm) == 100]

lines = read_file()
ingredients = []
for line in lines:
    make_ingredient_dict(line)
all_permutation = generate_permutations(len(ingredients))
# # Part 1
final_result = []
for permutation in all_permutation:
    capacity = []
    durabilty = []
    flavor = []
    texture = []
    permutation = list(permutation)
    for i in range(0,len(ingredients)):
        capacity.append(int(permutation[i]) * int(ingredients[i]["capacity"]))
        durabilty.append(int(permutation[i]) * int(ingredients[i]["durability"]))
        flavor.append(int(permutation[i]) * int(ingredients[i]["flavor"]))
        texture.append(int(permutation[i]) * int(ingredients[i]["texture"]))
    c =max(0,sum(capacity))
    d =max(0,sum(durabilty))
    f =max(0,sum(flavor))
    t =max(0,sum(texture))
    final_result.append([permutation,c*d*f*t])
maxi = 0
ratio = []
for f in final_result:
    if f[1] > maxi:
        maxi = f[1]
        ratio = f[0]
print("Part 1: ",ratio, "Ans: ", maxi )
# Part 2

ingredients = []
for line in lines:
    make_updated_ingredient_dict(line)
final_result = []
for permutation in all_permutation:
    capacity = []
    durabilty = []
    flavor = []
    texture = []
    calories = []
    permutation = list(permutation)
    for i in range(0,len(ingredients)):
        capacity.append(int(permutation[i]) * int(ingredients[i]["capacity"]))
        durabilty.append(int(permutation[i]) * int(ingredients[i]["durability"]))
        flavor.append(int(permutation[i]) * int(ingredients[i]["flavor"]))
        texture.append(int(permutation[i]) * int(ingredients[i]["texture"]))
        calories.append(int(permutation[i]) * int(ingredients[i]["calories"]))
    c =max(0,sum(capacity))
    d =max(0,sum(durabilty))
    f =max(0,sum(flavor))
    t =max(0,sum(texture))
    cal =sum(calories)
    if cal == 500:
        final_result.append([permutation,c*d*f*t])
maxi = 0
ratio = []
for f in final_result:
    if f[1] > maxi:
        maxi = f[1]
        ratio = f[0]
print("Part 2: ",ratio, "Ans: ", maxi )