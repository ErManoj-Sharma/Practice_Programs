def read_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    lines = [line.strip() for line in lines]

    array_2d = [lines[i:i+3] for i in range(0, len(lines), 3)]

    return array_2d

def find_common_elements(arr):
    list1 = []
    for i in arr:
      list1.append(list(set.intersection(*map(set, i))))
    return  list1 

def final_output(arr):
    sum=0
    for ans in arr:
      for i in range(len(ans)):
        if ans[i] >= 'A' and ans[i] <= 'Z':
            value = ord(ans[i])- 38
            sum = sum + value
        elif ans[i] >= 'a' and ans[i] <='z':
            value = ord(ans[i])- 96
            sum = sum + value
    return sum

filename = 'day3.txt'
result = read_file(filename)
ans = find_common_elements(result)
a = final_output(ans)
print(a)
