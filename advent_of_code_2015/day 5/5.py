def read_file():
    f = open("input.txt", "r")
    lines = f.readlines()
    f.close()
    return lines

def double_entry(s):
    for i in range(0,len(s)-1):
        if s[i] == s[i+1]:
            return True
    return False

def check_vowel(str):
    v_list = []
    for i in range(0, len(str)):
        if str[i] in ['a','e','i','o','u']:
            v_list.append(str[i])
    if len(v_list) >= 3:
        return True
    else:
        return False

def adjacent(string):
    invalid_substrings = ['ab', 'cd', 'pq', 'xy']
    for sub in invalid_substrings:
        if sub in string:
            return False
    return True

def repeat_one_letter(s):
    for i in range(0,len(s)-2):
        if s[i] == s[i+2]:
            return True
    return False

def has_repeated_pairs(s):
    for i in range(len(s) - 2):
        if s[i: i + 2] in s[i + 2:]:
            return True
    return False

lines = read_file()
# Part 1
count = 0
for line in lines:
    line = line.strip()
    flag1 = double_entry(line)
    flag2 = check_vowel(line)
    flag3 = adjacent(line)
    if flag1 and flag2 and flag3:
        count = count + 1
print("Part 1: ",count)
# Part 2
count = 0
for line in lines:
    line = line.strip()
    flag1 = repeat_one_letter(line)
    flag2 = has_repeated_pairs(line)
    if flag1 and flag2 :
        count = count + 1
print("Part 2: ",count)
