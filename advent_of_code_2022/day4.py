def read_file(filename):
  with open(filename, "r") as file:
    lines = file.readlines()  # Read all lines into a list
  return lines

def make_two_array(lines):
  list1, list2 = [], []
  for line in lines:
    line = line.strip()
    start,end = line.split(',')
    start = [int(i) for i in start.split('-')]
    end = [int(i) for i in end.split('-')]
    list1.append(start)
    list2.append(end)
  return list1,list2

def count(list1,list2):
  sum = 0
  for i in range(len(list1)):
    if(list1[i][0] <= list2[i][0] and list1[i][1] >= list2[i][1]) or (list1[i][0] >= list2[i][0] and list1[i][1] <= list2[i][1]):
      print(list1[i][0], list1[i][1],"-",list2[i][0],list2[i][1])
      print(sum)
      sum = sum + 1
  return sum
lines = read_file('day4.txt')
list1,list2 = make_two_array(lines)
sum = count(list1,list2)
print("sum is:",sum)
