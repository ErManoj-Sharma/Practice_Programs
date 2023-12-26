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

lines_array = read_file()
l=[]
points=[]
for line in lines_array:
    l.append(line[10:].strip().split("|"))
for i in range(0, len(l)):
    get_points(l[i])

print("Part 1: ",sum(points))