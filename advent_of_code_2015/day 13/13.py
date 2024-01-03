from itertools import permutations

def read_file():
    f = open("input.txt", "r")
    lines = f.readlines()
    f.close()
    return [line.strip() for line in lines]

def create_key_value_pairs(data):
    return {f"{entry[0]} to {entry[1]}": entry[2] for entry in data}

def generate_permutations(names):
    return list(permutations(names))

def get_next_happiness(A,B):
    key = f"{A} to {B}"
    return int(detail_dict[key])

def get_previous_happiness(B,A): 
    key = f"{A} to {B}"
    return int(detail_dict[key])

def make_instructions(line):
    parts = line.split(' ')
    p1, status, number, p2 = parts[0], parts[2], int(parts[3]), parts[10][:-1]
    return [p1, p2, number] if status == 'gain' else [p1, p2, -number]

def extract_unique_persons(instructions):
    unique_persons = []
    for i in instructions:
        if i[0] not in unique_persons:
            unique_persons.append(i[0])
    return unique_persons

def generate_all_permutations_as_lists(elements):
    return [list(permutation) for permutation in generate_permutations(elements)]

def calculate_happiness_for_permutations(all_permutations):
    result_arr = []
    for i in all_permutations:
        count = 0
        l = len(i)
        for j in range(l-1):
            count += get_next_happiness(i[j], i[j+1])
            count += get_previous_happiness(i[j], i[j+1])
        count += get_next_happiness(i[-1], i[0])
        count += get_previous_happiness(i[-1], i[0])
        result_arr.append([i, count])
    return result_arr

def find_max_value_and_index(arr):
    max_value = 0
    max_index = None
    for i, value in enumerate(arr):
        if value[1] > max_value:
            max_value = value[1]
            max_index = i
    return arr[max_index][0], max_value

def generate_new_happiness_entries(persons):
    new_happiness = []
    for i in persons:
        new_happiness.append(["ME", i, 0])
        new_happiness.append([i, "ME", 0])
    return new_happiness


lines = read_file()
instructions = []
for line in lines:
    instruction = make_instructions(line)
    instructions.append(instruction)
detail_dict = create_key_value_pairs(instructions)
total_person = extract_unique_persons(instructions)
all_permutations = generate_all_permutations_as_lists(total_person)
final_arr = calculate_happiness_for_permutations(all_permutations)
max_index, max_value = find_max_value_and_index(final_arr)
print("Part 1: List: ",max_index,"Answer: ",max_value)

new_happiness= generate_new_happiness_entries(total_person)
instructions.extend(new_happiness)
detail_dict = create_key_value_pairs(instructions)
total_person = extract_unique_persons(instructions)
all_permutations = generate_all_permutations_as_lists(total_person)
final_arr = calculate_happiness_for_permutations(all_permutations)
max_index, max_value = find_max_value_and_index(final_arr)
print("Part 2: List: ",max_index,"Answer: ",max_value)





