def read_file():
    f = open("input.txt", "r")
    lines = f.readlines()
    f.close()
    return list(line.replace("\n",'') for line in lines)

def print_2darray():
    global array_2d
    for i in range(0,len(array_2d)):
        for j in range(0,len(array_2d)):
            print(array_2d[i][j], end=" ")
        print()

def get_start_point():
    global array_2d
    for i in range(0,len(array_2d)):
        for j in range(0,len(array_2d)):
            if array_2d[i][j] == "^":
                return [i,j]
            if array_2d[i][j] == ">":
                return [i,j]
            if array_2d[i][j] == "<":
                return [i,j]
            if array_2d[i][j] == "v":
                return [i,j]
            
def movement(x,y):
    global array_2d
    global row
    global col
    if array_2d[x][y]=="^":
        p,q = x-1,y
        print("In ^")
        while array_2d[p][q] =="." or array_2d[p][q] =="X":
            array_2d[p+1][y]="X"
            array_2d[p][q]="^"
            p = p-1
            x=p
            if p == 0 and array_2d[p][q] == ".":
                array_2d[p][q]="X"
                array_2d[p+1][q] = "X"
                break

        if array_2d[x][y] == "#":
            array_2d[x+1][y] = ">"
            x,y = get_start_point()
            movement(x,y)
          
    if array_2d[x][y]==">":
        p,q = x,y+1
        print("in >")
        while array_2d[p][q] =="." or array_2d[p][q] =="X":
            array_2d[p][q-1]="X"
            array_2d[p][q]=">"
            q = q+1
            y=q
            if q == col and array_2d[p][q] == ".":
                array_2d[p][q]="X"
                array_2d[p][q-1] = "X"
                break

        if array_2d[x][y] == "#":
            array_2d[x][y-1] = "v"
            x,y = get_start_point()
            movement(x,y)

    if array_2d[x][y]=="<":
        p,q = x,y-1
        print("in <")
        while array_2d[p][q] =="." or array_2d[p][q] =="X":
            array_2d[p][q+1]="X"
            array_2d[p][q]="<"
            q = q-1
            y=q
            if q == 0 and array_2d[p][q] == ".":
                array_2d[p][q]="X"
                array_2d[p][q+1] = "X"
                break
            
        if array_2d[x][y] == "#":
            array_2d[x][y+1] = "^"
            x,y = get_start_point()
            movement(x,y)

    if array_2d[x][y]=="v":
        p,q = x+1,y
        print("in v")
        print(p,q)
        print("row",row)
        while array_2d[p][q] =="." or array_2d[p][q] =="X":
            array_2d[p-1][y]="X"
            array_2d[p][q]="v"
            p = p+1
            x=p
            if p == row and array_2d[p][q] == ".":
                array_2d[p-1][q] = "X"
                array_2d[p][q]="X"
                break

        if array_2d[x][y] == "#":
            array_2d[x-1][y] = "<"
            x,y = get_start_point()
            movement(x,y)

            
lines= read_file()
array_2d=[]

for line in lines:
    array_2d.append(list(line.replace("\n",'')))

row = len(array_2d)-1
col = len(array_2d)-1


start_point= get_start_point()
print("before movement")
movement(start_point[0],start_point[1])
print("after movement")
print()
print_2darray()

count = 0
for i in range(0, len(array_2d)):
    for j in range(0,len(array_2d)):
        if array_2d[i][j]=="X":
            count = count+1
print(count)