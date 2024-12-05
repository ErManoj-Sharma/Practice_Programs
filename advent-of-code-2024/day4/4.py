def read_file():
    f = open("input.txt", "r")
    lines = f.readlines()
    f.close()
    return list(lines)

array_2d = [] 
lines = read_file()
count=0

for line in lines:
    array_2d.append(list(line.replace("\n",'')))

def get_north(x,y):
    limit = 3
    if x < limit :
        return False
    string = array_2d[x][y]+array_2d[x-1][y]+array_2d[x-2][y]+array_2d[x-3][y] 
    if string == "XMAS":
        return True
    return False

def get_south(x,y):
    limit = len(line)-1
    if x > limit-3:
        return False
    string = array_2d[x][y]+array_2d[x+1][y]+array_2d[x+2][y]+array_2d[x+3][y] 
    if string == "XMAS":
        return True
    return False

def get_west(x,y):
    limit = 3
    if y < limit:
        return False
    string = array_2d[x][y]+array_2d[x][y-1]+array_2d[x][y-2]+array_2d[x][y-3] 
    if string == "XMAS":
        return True
    return False

def get_east(x,y):
    limit = len(line)-1
    if y > limit-3:
        return False
    string = array_2d[x][y]+array_2d[x][y+1]+array_2d[x][y+2]+array_2d[x][y+3] 
    if string == "XMAS":
        return True
    return False

def get_north_west(x,y):
    limit = 3
    if x < limit or y < limit:
        return False
    string = array_2d[x][y]+array_2d[x-1][y-1]+array_2d[x-2][y-2]+array_2d[x-3][y-3] 
    if string == "XMAS":
        return True
    return False

def get_north_east(x,y):
    limit = len(line)-1
    limit_x = 3
    if x < limit_x or y > limit-3:
        return False
    string = array_2d[x][y]+array_2d[x-1][y+1]+array_2d[x-2][y+2]+array_2d[x-3][y+3] 
    if string == "XMAS":
        return True
    return False

def get_south_west(x,y):
    limit = len(line)-1
    limit_y = 3
    if x > limit-3 or y < limit_y:
        return False
    string = array_2d[x][y]+array_2d[x+1][y-1]+array_2d[x+2][y-2]+array_2d[x+3][y-3] 
    if string == "XMAS":
        return True
    return False

def get_south_east(x,y):
    limit = len(line)-1
    if x > limit-3 or y > limit-3:
        return False
    string = array_2d[x][y]+array_2d[x+1][y+1]+array_2d[x+2][y+2]+array_2d[x+3][y+3] 
    if string == "XMAS":
        return True
    return False


for i in range(0,len(lines)):
    for j in range(0, len(lines)):
        if array_2d[i][j] == "X":
            if get_east(i,j):
                count = count + 1
            if get_west(i,j):
                count = count + 1
            if get_north(i,j):
                count = count + 1
            if get_south(i,j):
                count = count + 1
            if get_north_west(i,j):
                count = count + 1
            if get_north_east(i,j):
                count = count + 1
            if get_south_west(i,j):
                count = count + 1
            if get_south_east(i,j):
                count = count + 1
print(count)

# Part 2
cordinate_list=[]

def p2_get_north_west(x,y):
    global cordinate_list
    limit = 2
    if x < limit or y < limit:
        return False
    string = array_2d[x][y]+array_2d[x-1][y-1]+array_2d[x-2][y-2] 
    if string == "MAS":
        cordinate_list.append([x-1,y-1])
        return True
    return False

def p2_get_north_east(x,y):
    global cordinate_list
    limit = len(line)-1
    limit_x = 2
    if x < limit_x or y > limit-2:
        return False
    string = array_2d[x][y]+array_2d[x-1][y+1]+array_2d[x-2][y+2]
    if string == "MAS":
        cordinate_list.append([x-1,y+1])
        return True
    return False

def p2_get_south_west(x,y):
    global cordinate_list
    limit = len(line)-1
    limit_y = 2
    if x > limit-2 or y < limit_y:
        return False
    string = array_2d[x][y]+array_2d[x+1][y-1]+array_2d[x+2][y-2] 
    if string == "MAS":
        cordinate_list.append([x+1,y-1])
        return True
    return False

def p2_get_south_east(x,y):
    global cordinate_list
    limit = len(line)-1
    if x > limit-2 or y > limit-2:
        return False
    string = array_2d[x][y]+array_2d[x+1][y+1]+array_2d[x+2][y+2]
    if string == "MAS":
        cordinate_list.append([x+1,y+1])
        return True
    return False

for i in range(0,len(lines)):
    for j in range(0, len(lines)):
        if array_2d[i][j] == "M":
            p2_get_north_west(i,j)
            p2_get_north_east(i,j)
            p2_get_south_west(i,j)
            p2_get_south_east(i,j)
print(cordinate_list)
result = [item for item in cordinate_list if cordinate_list.count(item) > 1]
print(result)
print(len(result)/2)