def read_file():
    f = open("input.txt", "r")
    lines = f.readlines()
    f.close()
    return list(lines)

lines = read_file()
left_list=[]
right_list=[]
for i in range(0,len(lines)):
    left_list.append(int(lines[i].split()[0]))
    right_list.append(int(lines[i].split()[1]))

left = sorted(left_list)
right = sorted(right_list)

final_list=[]
for i in range(0,len(lines)):
    res = abs(left[i]-right[i])
    final_list.append(res)

# Part 1
print(sum(final_list))

# Part 2
def no_of_occurence(num,list1):
    count = 0
    for a in list1:
        if num == a:
            count = count+1
    return count


left = sorted(left_list)
right = sorted(right_list)
final_list2 =[]
for i in range(0,len(left)):
    final_list2.append(left[i] * no_of_occurence(left[i], right))
print(sum(final_list2))