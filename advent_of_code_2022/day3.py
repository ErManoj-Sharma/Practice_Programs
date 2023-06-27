def read_file(filename):
    with open(filename, 'r') as file:
        list1=[]
        list2=[]
        for line in file:
            line = line.strip()
            half = int(len(line)/2)
            list1.append(line[0:half])
            list2.append(line[half:])
    return list1,list2

def find_common_chr(list1,list2):
    ans = []
    for i in range(len(list1)):
        ans.append(''.join(set(list1[i]).intersection(list2[i])))
    return ans

def final_output(ans):
    sum=0
    for i in range(len(ans)):
      if ans[i] >= 'A' and ans[i] <= 'Z':
          value = ord(ans[i])- 38
          sum = sum + value
      elif ans[i] >= 'a' and ans[i] <='z':
          value = ord(ans[i])- 96
          sum = sum + value
    return sum
filename = 'day3.txt'
list1,list2 = read_file(filename)
print(list1)
print(list2)
ans = find_common_chr(list1,list2)
print(ans)
sum = final_output(ans)
print(sum)