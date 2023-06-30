stack = [['B','W','N'],['L','Z','S','P','T','D','M','B'],['Q','H','Z','W','R'],['W','D','V','J','Z','R'],
         ['S','H','M','B'],['L','G','N','J','H','V','P','B'],['J','Q','Z','F','H','D','L','S'],
         ['W','S','F','J','G','Q','B'],['Z','W','M','S','C','D','J']]
for i in range(len(stack)):
    print(i+1 ,":",stack[i],end="\n")



def read_file(filename):
  with open(filename, "r") as file:
    lines = file.readlines()  # Read all lines into a list
  return lines

def make_two_array(lines):
  list1= []
  for line in lines:
    line = line.strip()
    line = line.split(' ')
    list1.append([line[1],line[1],line[5]])
  return list1

lines = read_file('day5.txt')
list1 = make_two_array(lines)
print(list1)





# str = 'move 4 from 7 to 2'
# list = []
# print(str.strip())
# print(str.split(' '))
# s = str.split(' ')
# list.append([s[1],s[1],s[5]])
# print(list)
