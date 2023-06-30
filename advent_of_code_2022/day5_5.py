stack = [['Z','N'],['M','C','D'],['P']]
# for i in range(len(stack)):
#     print(i+1 ,":",stack[i],end="\n")



def read_file(filename):
  with open(filename, "r") as file:
    lines = file.readlines()  # Read all lines into a list
  return lines

def make_two_array(lines):
  list1 = []
  for line in lines:
    line = line.strip()
    line = line.split(' ')
    list1.append([line[1],line[3],line[5]])
  return list1

def mov(ele,listfrom,listto):
  for i in range(ele):
    temp = listfrom[-1]
    listto.append(temp)
    listfrom.pop()
  return 

def move_stack(list1):
  for i in range(len(list1)):
    ele = int(list1[i][0])
    listfrom = int(list1[i][1])
    listto = int(list1[i][2])
    mov(ele,stack[listfrom-1],stack[listto-1])
  return 1

lines = read_file('day5_5.txt')
list1 = make_two_array(lines)
move_stack(list1)
l = []
for i in range(len(stack)):
  l.append(stack[i][-1])
print(l)
