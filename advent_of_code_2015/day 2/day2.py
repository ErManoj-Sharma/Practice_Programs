def read_file():
    f = open("input.txt", "r")
    lines = f.readlines()
    f.close()
    return list(lines)

def get_area(l,b,h):
    x = l*b
    y = b*h
    z = h*l
    m = min([x,y,z])
    return int((2 *(x+y+z))+ m)

def get_ribbin(le,b,h):
    ll = sorted([le,b,h])
    return int((2 * int(ll[0]) )+(2 * int(ll[1]) )+(le*b*h))

lines = read_file()
area = []
ribbin=[]
dimension = [line.strip().split('x') for line in lines]
for i in range(0, len(dimension)):
    a = get_area(int(dimension[i][0]),int(dimension[i][1]),int(dimension[i][2]))
    b = get_ribbin(int(dimension[i][0]),int(dimension[i][1]),int(dimension[i][2]))
    area.append(a)
    ribbin.append(b)
print(sum((area)))
print(sum(ribbin))