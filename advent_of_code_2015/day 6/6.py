def read_file():
    f = open("input.txt", "r")
    lines = f.readlines()
    f.close()
    return lines

def make_instruction(line):
    task = None
    start_x = None
    start_y = None
    end_x = None
    end_y = None
    if line.startswith('turn on'):
        line = line[7:]
        line = line.strip().split('through')
        start = line[0].strip().split(',')
        end = line[1].strip().split(',')
        task,start_x,start_y,end_x,end_y  = 'on', start[0],start[1],end[0],end[1]
    elif line.startswith('turn off'):
        line = line[8:]
        line = line.strip().split('through')
        start = line[0].strip().split(',')
        end = line[1].strip().split(',')
        task,start_x,start_y,end_x,end_y  = 'off', start[0],start[1],end[0],end[1]
        pass
    elif line.startswith('toggle'):
        line = line[6:]
        line = line.strip().split('through')
        start = line[0].strip().split(',')
        end = line[1].strip().split(',')
        task,start_x,start_y,end_x,end_y  = 'toggle', start[0],start[1],end[0],end[1]
        pass
    return [task, start_x,start_y, end_x,end_y]

def on(start_x, start_y, end_x, end_y):
    global light
    for i in range(start_x, end_x+1):
        for j in range(start_y,end_y+1):
            light[i][j] = '*'

def off(start_x, start_y, end_x,end_y):
    global light
    for i in range(start_x, end_x+1):
        for j in range(start_y,end_y+1):
            light[i][j] = '.'

def toggle(start_x, start_y, end_x,end_y):
    global light
    for i in range(start_x, end_x+1):
        for j in range(start_y,end_y+1):
            if light[i][j] == '*':
                light[i][j] = '.'
            else:
                light[i][j] = '*'
def onp2(start_x, start_y, end_x, end_y):
    global light
    for i in range(start_x, end_x+1):
        for j in range(start_y,end_y+1):
            light[i][j] = int(light[i][j]) + 1
            if light[i][j] < 0:
                light[i][j] = 0

def offp2(start_x, start_y, end_x,end_y):
    global light
    for i in range(start_x, end_x+1):
        for j in range(start_y,end_y+1):
            light[i][j] = int(light[i][j]) - 1
            if light[i][j] < 0:
                light[i][j] = 0

def togglep2(start_x, start_y, end_x,end_y):
    global light
    for i in range(start_x, end_x+1):
        for j in range(start_y,end_y+1):
                light[i][j] =  int(light[i][j]) + 2
                if light[i][j] < 0:
                    light[i][j] = 0


total = 1000
light = [['.'] * total for _ in range(total)]
rows = len(light[0])
col = len(light[1])
lines = read_file()
instructions=[]
for line in lines:
   ins = make_instruction(line.strip())
   instructions.append(ins)

# Part 1
for instruction in instructions:
    if instruction[0] == 'on':
        on(int(instruction[1]),int(instruction[2]),int(instruction[3]),int(instruction[4]))
    elif instruction[0] =='off':
        off(int(instruction[1]),int(instruction[2]),int(instruction[3]),int(instruction[4]))
    elif instruction[0] == 'toggle':
        toggle(int(instruction[1]),int(instruction[2]),int(instruction[3]),int(instruction[4]))

count = 0
for i in range(0,rows):
    for j in range(0,col):
        if light[i][j] == '*':
            count = count + 1
print("Part 1: ",count)

# Part 2
light = [[0] * total for _ in range(total)]
for instruction in instructions:
    if instruction[0] == 'on':
        onp2(int(instruction[1]),int(instruction[2]),int(instruction[3]),int(instruction[4]))
    elif instruction[0] =='off':
        offp2(int(instruction[1]),int(instruction[2]),int(instruction[3]),int(instruction[4]))
    elif instruction[0] == 'toggle':
        togglep2(int(instruction[1]),int(instruction[2]),int(instruction[3]),int(instruction[4]))

count = 0
for i in range(0,rows):
    for j in range(0,col):
        if light[i][j] > 0:
            count = count + light[i][j]
print("Part 2: ", count)