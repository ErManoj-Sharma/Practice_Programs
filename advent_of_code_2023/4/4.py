def read_file():
    f = open("input.txt", "r")
    lines = f.readlines()
    f.close()
    return lines

def get_points(arr):
    global points
    a1 = list(filter(lambda x: x != '', arr[0].strip().split(" ")))
    a2 = list(filter(lambda x: x != '', arr[1].strip().split(" ")))
    common_ele = [i for i in a1 if i in a2]
    points.append(int(pow(2, len(common_ele)-1)))

def get_total_instance(arr, index):
    global scratchcard
    element_count = scratchcard[index]
    a1 = list(filter(lambda x: x != '', arr[0].strip().split(" ")))
    a2 = list(filter(lambda x: x != '', arr[1].strip().split(" ")))
    common_ele = [i for i in a1 if i in a2]
    if len(common_ele) > 0:
        for i in range(1,len(common_ele)+1):
            scratchcard[index+i] = scratchcard[index+i] + element_count * 1
    pass

lines_array = read_file()
# Part 1
l=[]
points=[]
for line in lines_array:
    l.append(line[8:].strip().split("|"))
for i in range(0, len(l)):
    get_points(l[i])

print("Part 1: ",sum(points))
# Part 2

scratchcard = {key: 1 for key in range(1, len(lines_array)+1)}
for i in range(0, len(l)):
    get_total_instance(l[i], i+1)
final = sum(list(scratchcard.values()))
print("Part 2: ", final)