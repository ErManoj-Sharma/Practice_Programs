from collections import OrderedDict
def read_file():
    f = open("input.txt", "r")
    lines = f.readline()
    f.close()
    return list(lines)
def remove_duplicate(arr):
    return list(OrderedDict.fromkeys(tuple(element) for element in arr))
def get_santa_robo(line):
    santa = []
    robo = []
    for m in range(0, len(line)):
        if m % 2 == 0:
            santa.append(line[m])
        else:
            robo.append(line[m])
    return santa, robo

def deliver_gift(chr):
    global i
    global j
    if chr == '^':
        i = i - 1
    elif chr == 'v':
        i = i + 1
    elif chr == '<':
        j = j - 1
    elif chr == '>':
        j = j + 1
    return [i, j]  # Append the updated coordinates to the list

i,j=0,0
line = read_file()
l = [[i,j]]
# Part 1
for k in range(0, len(line)):
    l.append(deliver_gift(line[k]))

unique_list = remove_duplicate(l)
print("Part 1: ",len(unique_list))

# Part 2 
santa,robo = get_santa_robo(line)
i,j=0,0
santa_list=[[0,0]]
for k in range(0, len(santa)):
    santa_list.append(deliver_gift(santa[k]))

i,j=0,0
robo_list=[[0,0]]
for k in range(0, len(robo)):
    robo_list.append(deliver_gift(robo[k]))
final_list = remove_duplicate(santa_list + robo_list)

print("Part 2: ",len(final_list))
