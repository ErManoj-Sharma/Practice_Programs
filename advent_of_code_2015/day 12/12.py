import re
import json
def read_file():
    f = open("input.txt", "r")
    lines = f.readline()
    f.close()
    return lines.strip()



     
    
line = read_file()
# Part 1
pattern = r'-?\d+'
l = re.findall(pattern, line)
ans = 0
for i in l:
    ans = ans + int(i)
print("Part 1: ",ans)
# part 2

js = json.loads(line)
def num_count(js):
    if type(js) is int:
        return js 
    if type(js) is str:
        return 0 
    if type(js) is list:
        return sum(num_count(z) for z in js)
    if "red" in js.keys() or  "red" in js.values():
        return 0
    return sum(num_count(k) + num_count(v) for k, v in js.items())

print("Part 2: ",num_count(js))