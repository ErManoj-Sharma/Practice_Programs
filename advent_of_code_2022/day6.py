def read_file(filename):
  with open(filename, "r") as file:
    text = file.read()
  return text

def find_index(file_text):
  list1 = list(file_text)
  temp = []
  index = 0
  for i in range(len(list1)):
      temp  = list1[i:i+4]
      list2 = list(set(temp))
      if (len(list2) == 4):
          index = i+4
          break
  return index

def find_index2(file_text):
  list1 = list(file_text)
  temp = []
  index = 0
  for i in range(len(list1)):
      temp  = list1[i:i+14]
      list2 = list(set(temp))
      if (len(list2) == 14):
          index = i+14
          break
  return index

file_text = read_file('day6.txt')
index = find_index(file_text)
index2 = find_index2(file_text)
print(index)
print(index2)