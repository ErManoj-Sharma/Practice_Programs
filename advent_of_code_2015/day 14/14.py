def read_file():
    f = open("input.txt", "r")
    lines = f.readlines()
    f.close()
    return lines

def make_instructions(lines):
    global reindeer
    instruction = []
    for line in lines:
        name = line.split(' ')[0]
        speed = line.split(' ')[3]
        time = line.split(' ')[6]
        rest = line.split(' ')[13]
        reindeer[name] = (int(speed), int(time),int(rest))
        instruction.append([name,int(speed),int(time),int(rest)])
    return instruction

def distance_after_time(instruction,time):
    distance = 0
    speed = instruction[1] * instruction[2] 
    t = instruction[2] + instruction[3]
    time_remaining = time % t
    time_used = int(time / t)
    distance = time_used * speed
    if time_remaining / instruction[2] > 0 :
        distance = distance + instruction[1] * instruction[2] 
    return distance

def get_dist(r, stop_time):
    t=0
    d=[0]
    speed ,end ,rest = reindeer[r]
    while t < stop_time:
        for _ in range(end):
            d.append(d[-1]+speed)
            t+=1
            if t == stop_time:
                return d 
        for _ in range(rest):
            d.append(d[-1])
        t+= rest
    return d

endtime = 2503
lines = read_file()
reindeer = {}
instruction = make_instructions(lines)
# Part 1 
ans = []
for i in instruction:
    result = distance_after_time(i,endtime)
    ans.append(result)
print("Part 1: ",max(ans))
# Part 2
for r in reindeer.keys():
    print(r)
dist_tables = {r: get_dist(r, endtime) for r in reindeer.keys() }
points  = {r:0 for r in reindeer.keys()}
for t in range(1,endtime):
    lead = max(dist_tables[r][t] for r in reindeer.keys())
    for r in reindeer.keys():
        if dist_tables[r][t] == lead:
            points[r]+=1
print("Part 2: ",max(points.values()))
