def read_file():
    f = open("input.txt", "r")
    lines = f.readlines()
    f.close()
    return lines

def get_first_digit(input_string):
    for char in input_string:
        if char.isdigit():
            return int(char)
    return None 
            
def match_word(str):
    for i in range(0, len(list(str))):
        if str[i].isdigit():
            return int(str[i])
            break
        else:
            if ''.join(list(str)[0:i+1]).find("one") > -1 or ''.join(list(str)[0:i+1]).find("eno") > -1:
                return 1   
                break
            if ''.join(list(str)[0:i+1]).find("two") > -1 or ''.join(list(str)[0:i+1]).find("owt") > -1:
                return 2
                break
            if ''.join(list(str)[0:i+1]).find("three") > -1 or ''.join(list(str)[0:i+1]).find("eerht") > -1:
                return 3
                break
            if ''.join(list(str)[0:i+1]).find("four") > -1 or ''.join(list(str)[0:i+1]).find("ruof") > -1:
                return 4    
                break
            if ''.join(list(str)[0:i+1]).find("five") > -1 or ''.join(list(str)[0:i+1]).find("evif") > -1:
                return 5    
                break
            if ''.join(list(str)[0:i+1]).find("six") > -1 or ''.join(list(str)[0:i+1]).find("xis") > -1:
                return 6    
                break
            if ''.join(list(str)[0:i+1]).find("seven") > -1 or ''.join(list(str)[0:i+1]).find("neves") > -1:
                return 7    
                break
            if ''.join(list(str)[0:i+1]).find("eight") > -1 or ''.join(list(str)[0:i+1]).find("thgie") > -1:
                return 8    
                break
            if ''.join(list(str)[0:i+1]).find("nine") > -1 or ''.join(list(str)[0:i+1]).find("enin") > -1:
                return 9
                break

# Part 1
num_array= []
lines_array = read_file()
for line in lines_array:
        first_num = get_first_digit(line)
        second_num = get_first_digit(line[::-1])
        num_array.append((first_num*10) + second_num)
print("Day 1 Problem 1: ", sum(num_array))

# Part 2
num_array= []
for line in lines_array:
        first_num = match_word(line)
        second_num = match_word(line[::-1])
        num_array.append((first_num*10) + second_num)
print("Day 1 Problem 2: ", sum(num_array))




    
    
