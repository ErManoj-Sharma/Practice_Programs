def read_file():
    f = open("input.txt", "r")
    lines = f.readline()
    f.close()
    return list(lines)

lines = read_file()
count = 0
index=0
for i in range(0,len(lines)):
    if lines[i] == '(':
        count += 1
    if lines[i] == ')':
        if count == 0:
            index = i+1
            break
        count -= 1
print(count)
print(index)