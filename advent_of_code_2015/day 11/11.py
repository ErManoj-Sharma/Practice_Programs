def read_file():
    f = open("input.txt", "r")
    lines = f.readlines()
    f.close()
    return lines

# generate sequence
def generate_sequence():
    global line
    sequence = [line]
    while True:
        last_item = sequence[-1]
        next_item = increment_string(last_item)
        sequence.append(next_item)
        yield next_item

# incremet the string sequence
def increment_string(s):
    result = list(s)
    i = len(result) - 1
    while i >= 0:
        if result[i] == 'z':
            result[i] = 'a'
            i -= 1
        else:
            result[i] = chr(ord(result[i]) + 1)
            break
    else:
        result.insert(0, 'a')

    return ''.join(result)

# check condition 1
def check_increment_str(s):
    l = len(s)
    flag = False
    for i in range(0,l-2):
        s1 = ord(s[i])
        s2 = ord(s[i+1])
        s3 = ord(s[i+2])
        if s2-s1 == 1 and s3-s2 == 1 and s3-s1 == 2:
            flag = True
    return flag

# check condition 2
def check_i_o_l(s):
    flag = True 
    l = len(s)
    for i in range(0,l):
        if s[i] == 'i' or s[i] =='0' or s[i] == 'l':
            flag = False
    return flag

# check condition 3
def check_double_char(s):
    flag = False
    l = len(s)
    count = 0
    ch = []
    for i in range(0,l-1):
        if s[i] == s[i+1]:
            if s[i] not in ch:
                count += 1
                ch.append(s[i])
    if count > 1:
        flag = True 
    return flag

# check valid password
def check_valid_password(password):
    flag1 = check_increment_str(password)
    flag2 = check_i_o_l(password)
    flag3 = check_double_char(password)
    return flag1 and flag2 and flag3

# Make a new password 
def get_new_password():
    while True:
        password = next(sequence_generator)
        if password < 'zzzzzzzz':
            flag = check_valid_password(password)
            if flag:
                return password
        else:
            break

lines = read_file()
sequence_generator = generate_sequence()
for line in lines:
    line = line.strip()
    password = get_new_password()
    print("Part1 Password: ", password)
    line = password.strip()
    password = get_new_password()
    print("Part2 Password: ", password)
