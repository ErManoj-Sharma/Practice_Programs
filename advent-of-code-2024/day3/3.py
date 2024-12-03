import re
def read_file():
    f = open("input.txt", "r")
    lines = f.readline()
    f.close()
    return lines

pattern = r"mul\(([0-9]+),([0-9]+)\)"

# Part 1 Ans
line = read_file()
matched_pattern = re.findall(pattern,line)
mul_list=[]

for i in range(0,len(matched_pattern)):
    lst = list(matched_pattern[i])    
    mul_list.append(int(lst[0])*int(lst[1]))

print("Part1: ",sum(mul_list))

# Part 2 Ans
mul_list=[]
string = read_file()
pattern2 = r"don't\(\).*?do\(\)"
result = re.sub(pattern2, "", string)
matched_pattern = re.findall(pattern,result)
mul_list=[]

for i in range(0,len(matched_pattern)):
    lst = list(matched_pattern[i])    
    mul_list.append(int(lst[0])*int(lst[1]))

print("Part 2: ",sum(mul_list))