def read_file(filename):
  with open(filename, "r") as file:
      lines = file.readlines()  # Read all lines into a list

  first_chars = []
  second_chars = []

  for line in lines:
      if len(line) >= 2:  
          first_chars.append(line[0])
          second_chars.append(line[2])
  return first_chars,second_chars

def calculate_score_part1(first,second):
  win_score = 0
  for i in range(2500):
    if first[i] == 'A':              # Rock
       if second[i] == 'X':          # rock
          win_score = win_score + 4   #(2+3)
       elif second[i] == 'Y':          #paper
          win_score = win_score + 8   #(2+6)
       else:
          win_score = win_score + 3   #(scssor,(3+0))
    
    elif first[i] == 'B':                 # paper
       if second[i] == 'X':            #rock
          win_score = win_score + 1   #(1+0)
       elif second[i] == 'Y':           #paper
          win_score = win_score + 5    #(2+3)
       else:                             #scssor
          win_score = win_score +  9   # 3+6
    elif first[i] == 'C':
       if second[i] == 'X':            #rock
          win_score = win_score + 7   #(1+6)
       elif second[i] == 'Y':           #paper
          win_score = win_score + 2    #(2+0)
       else:                             #scssor
          win_score = win_score +  6   # 3+3
  return win_score

def calculate_score_part2(first,second):
  win_score = 0
  for i in range(2500):
    if first[i] == 'A':              # Rock
       if second[i] == 'X':          # rock
          win_score = win_score + 3   #(2+3)
       elif second[i] == 'Y':          #paper
          win_score = win_score + 4   #(2+6)
       else:
          win_score = win_score + 8   #(scssor,(3+0))
    
    elif first[i] == 'B':                 # paper
       if second[i] == 'X':            #rock
          win_score = win_score + 1   #(1+0)
       elif second[i] == 'Y':           #paper
          win_score = win_score + 5    #(2+3)
       else:                             #scssor
          win_score = win_score +  9   # 3+6
    elif first[i] == 'C':
       if second[i] == 'X':            #rock
          win_score = win_score + 2   #(1+6)
       elif second[i] == 'Y':           #paper
          win_score = win_score + 6    #(2+0)
       else:                             #scssor
          win_score = win_score + 7   # 3+3
  return win_score

first , second = read_file('day2.txt')
result = calculate_score_part1(first,second)
print(result)
result = calculate_score_part2(first,second)
print(result)