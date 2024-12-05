def read_file():
    f = open("test1.txt", "r")
    lines = f.readlines()
    f.close()
    return list(line.replace("\n",'') for line in lines)
def read_file2():
    f = open("test2.txt", "r")
    lines = f.readlines()
    f.close()
    return list(line.replace("\n",'') for line in lines)

lines = read_file()
lines2  =read_file2()

output1 =[]
ordering_rule=[]
update_lists=[]
clear_files_index=[]

for line in lines:
    ordering_rule.append(line.split("|"))

for line in lines2:
    line = line.split(",")
    update_lists.append([[line[i], line[i + 1]] for i in range(len(line) - 1)])

for i in range(0,len(update_lists)):
    if all(item in ordering_rule for item in update_lists[i]):
        index = update_lists.index(update_lists[i])
        clear_files_index.append(index)
        mid_index = len(update_lists[i]) // 2
        mid_element = update_lists[i][mid_index][0]
        output1.append(int(mid_element))

# Part 1
print(sum(output1))

