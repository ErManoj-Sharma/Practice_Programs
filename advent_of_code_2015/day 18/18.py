def read_file():
    f = open("input.txt", "r")
    lines = f.readlines()
    f.close()
    return [list(line.rstrip()) for line in lines ]

def filter_list(arr):
    res = []
    [res.append(x) for x in arr if x not in res and not x.isdigit() and x != "."]
    return res
def get_neighbors(matrix, x, y):
    neighbors = []
    rows, cols = len(matrix), len(matrix[0])

    for i in range(-1, 2):
        for j in range(-1, 2):
            new_x, new_y = x + i, y + j

            # Check if the new coordinates are within the bounds of the matrix
            if 0 <= new_x < rows and 0 <= new_y < cols:
                # Exclude the center element (x, y)
                if (i, j) != (0, 0):
                    neighbors.append(matrix[new_x][new_y])
    return neighbors

def count_on_light(arr):
    r = len(arr)
    c = len(arr[0])
    count = 0
    for i in range(0,r):
        for j in range(0,c):
            if arr[i][j] == '#':
                count = count+1
    return count

def display_arr(lines):
    row = len(lines)
    col = len(lines[0])
    for i in range(0,row):
        for j in range(0,col):
            print(lines[i][j], end=' ')
        print()

lines  = read_file()
steps = 100
row = len(lines)
col = len(lines[0])

# Part 1
new_lines = [['0' for _ in range(col)] for _ in range(row)]
for _ in range(steps):
    for i in range(0,row):
        for j in range(0,col):
            neighbour = get_neighbors(lines,i,j)
            on_neighbour = neighbour.count('#')
            off_neighbour = neighbour.count('.')

            # light is off
            if lines[i][j] == '.':
                if on_neighbour == 3:
                    new_lines[i][j] = '#'
                else:
                    new_lines[i][j] = '.'
            # Light is On
            if lines[i][j] == '#':
                if on_neighbour == 2 or on_neighbour == 3:
                   new_lines[i][j] = '#'
                else:
                   new_lines[i][j] = '.'
    lines = new_lines
    new_lines = [['0' for _ in range(col)] for _ in range(row)]
result = count_on_light(lines)
print("Part 1: ",result)

# Part 2
lines  = read_file()
steps = 100
row = len(lines)
col = len(lines[0])
new_lines = [['0' for j in range(col)] for i in range(row)]
for _ in range(steps):
    for i in range(0,row):
        for j in range(0,col):
            neighbour = get_neighbors(lines,i,j)
            on_neighbour = neighbour.count('#')
            off_neighbour = neighbour.count('.')

            # light is off
            if lines[i][j] == '.':
                if on_neighbour == 3:
                    new_lines[i][j] = '#'
                else:
                    new_lines[i][j] = '.'
            # Light is On
            if lines[i][j] == '#':
                if on_neighbour == 2 or on_neighbour == 3:
                   new_lines[i][j] = '#'
                else:
                   new_lines[i][j] = '.'
            if (i == 0 and j == 0) or (i == 0 and j == col-1) or (i == row-1 and j == 0) or (i == row-1 and j == col-1):
                new_lines[i][j] = '#'
    lines = new_lines
    new_lines = [[ '0' for j in range(col)] for i in range(row)]

result = count_on_light(lines)
print("Part 2: ",result)