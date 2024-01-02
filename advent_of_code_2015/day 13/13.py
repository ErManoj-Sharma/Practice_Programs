from itertools import permutations
def read_file():
    f = open("input.txt", "r")
    lines = f.readlines()
    f.close()
    return lines

def create_key_value_pairs(data):
    key_value_pairs = {}

    for entry in data:
        key = f"{entry[0]} to {entry[1]}"
        value = entry[2]
        key_value_pairs[key] = value

    return key_value_pairs

def generate_permutations(names):
    return list(permutations(names))
def get_next_happiness(A,B):
    key = f"{A} to {B}"
    return int(detail_dict[key])
def get_previous_happiness(B,A): 
    key = f"{A} to {B}"
    return int(detail_dict[key])
def make_instructions(l):
    p1 = l.split(' ')[0]
    status = l.split(' ')[2]
    if status == 'gain':
        number = int(l.split(' ')[3])
    else:
        number = 0 - int(l.split(' ')[3])
    p2 = l.split(' ')[10][:-1:]
    return [p1,p2,number]

lines = read_file()
instructions = []
for line in lines:
    line = line.strip()
    instruction = make_instructions(line)
    instructions.append(instruction)
detail_dict = create_key_value_pairs(instructions)
total_person = []
for i in instructions:
    if i[0] not in total_person:
        total_person.append(i[0])
all_permutations = []
for permutation in generate_permutations(total_person):
    all_permutations.append(list(permutation))
final_arr = []
for i in all_permutations:
    count = 0
    l = len(i)
    for j in range(l-1):
        count = count +  get_next_happiness(i[j], i[j+1])
        count = count + get_previous_happiness(i[j], i[j+1])
    count = count + get_next_happiness(i[-1],i[0])
    count = count + get_previous_happiness(i[-1], i[0])
    final_arr.append([i,count])
max = 0
index = None
for arr in final_arr:
    if arr[1] > max:
        max = arr[1]
        index = arr
print("Part 1: List: ",index,"Answer: ",index[1])
