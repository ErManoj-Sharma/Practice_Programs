from functools import cmp_to_key
def read_file():
    f = open("input1.txt", "r")
    lines = f.readlines()
    f.close()
    return list(line.replace("\n",'') for line in lines)

def read_file2():
    f = open("input2.txt", "r")
    lines = f.readlines()
    f.close()
    return list(line.replace("\n",'') for line in lines)


lines = read_file()
lines2 = read_file2()

output1 =[]
ordering_rule=[]
update_lists=[]

for line in lines:
    ordering_rule.append(line.split("|"))

for line in lines2:
    line = line.split(",")
    update_lists.append([[line[i], line[i + 1]] for i in range(len(line) - 1)])

for i in range(0,len(update_lists)):
    if all(item in ordering_rule for item in update_lists[i]):
        mid_index = len(update_lists[i]) // 2
        mid_element = update_lists[i][mid_index][0]
        output1.append(int(mid_element))
# Part 1
print(sum(output1))



p1,p2 = open('input.txt').read().split('\n\n')

rules = {}

for line in p1.splitlines():
    a,b = line.split('|')
    rules.setdefault(int(a),set()).add(int(b))

updates = [[*eval(line)] for line in p2.splitlines()]

def incorrect(r):
    return any(rules.get(n, set()).intersection(r[:i]) for i,n in enumerate(r))

print('part 2:', sum(sorted(r, key=cmp_to_key(lambda a,b: (a in rules.get(b))-1))[len(r)//2]
                     for r in filter(incorrect, updates)))