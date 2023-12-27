import hashlib
def read_file():
    f = open("input.txt", "r")
    lines = f.readline()
    f.close()
    return lines
line = read_file()  
i=0
part1=None
part2=None
while True:
    s = line+str(i)
    result = hashlib.md5(s.encode('UTF-8')).hexdigest()
    if result[0:5] == '00000' and part1 is None:
        part1 = i
    if result[0:6] == '000000':
        part2 = i
        break
    i = i+1
print("Part 1: ", part1)
print("Part 2: ", part2)