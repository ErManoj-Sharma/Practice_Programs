import re
def read_file():
    f = open("input.txt", "r")
    lines = f.readlines()
    f.close()
    return lines

lines = read_file()
total_count = []
s = ''
reverseCount = 0
for line in lines:
    line = line.strip()
    total_count.append(len(list(line)))
    s = s+line.strip()[1:-1]
    reverseCount += line.count('\\') + line.count('"') + len(line) + 2
eval = re.sub(r'\\x..|\\.', '*', s)

print('Part 1 answer is {0} - {1} = {2}'.format(sum(total_count), len(eval), sum(total_count)-len(eval)))
print('Part 2 answer is {0} - {1} = {2}'.format(reverseCount, sum(total_count), reverseCount - sum(total_count)))