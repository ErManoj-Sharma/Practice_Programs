def read_file():
    f = open("input.txt", "r")
    lines = f.readlines()
    f.close()
    return lines

def check_valid_game(games):
    status = True
    game_len = len(games)
    for i in range(game_len):
        sub_game = games[i].strip().split(',')
        sub_game_len = len(sub_game)
        for j in range(sub_game_len):
            if sub_game[j].strip().split()[1] == 'red' and int(sub_game[j].strip().split()[0]) > 12:
                status=False
                return status 
            elif sub_game[j].strip().split()[1] == 'blue' and int(sub_game[j].strip().split()[0]) > 14:
                status=False
                return status 
            elif sub_game[j].strip().split()[1] == 'green' and int(sub_game[j].strip().split()[0]) > 13:
                status=False
                return status 
    return status

def make_power_set(games):
    max_red = 0
    max_green=0
    max_blue=0
    game_len = len(games)
    for i in range(game_len):
        sub_game = games[i].strip().split(',')
        sub_game_len = len(sub_game)
        for j in range(sub_game_len):
            if sub_game[j].strip().split()[1] == 'red' and int(sub_game[j].strip().split()[0]) > max_red:
                max_red = int(sub_game[j].strip().split()[0])
            elif sub_game[j].strip().split()[1] == 'blue' and int(sub_game[j].strip().split()[0]) > max_blue:
                max_blue = int(sub_game[j].strip().split()[0])
            elif sub_game[j].strip().split()[1] == 'green' and int(sub_game[j].strip().split()[0]) > max_green:
                max_green = int(sub_game[j].strip().split()[0])
    return max_green * max_blue * max_red
        
def possbile_game(l,index):
    global final_array
    global final_array2
    status = check_valid_game(l)
    if status:
        final_array.append(index)
    ans = make_power_set(l)
    final_array2.append(ans)

lines_array = read_file()
i = 0
final_array= []
final_array2 = []
for line in lines_array:
    i = i+1
    possbile_game(line[8:].split(";"), i)
# Part 1
# print(final_array)
print("Part 1: ",sum(final_array))

# Part 2
# print(final_array2)
print("Part 2:",sum(final_array2))
