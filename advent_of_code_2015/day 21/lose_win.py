def read_file():
    f = open("input.txt", "r")
    lines = f.readlines()
    f.close()
    return lines
def read_hit_point_file():
    f = open("hit_points.txt", "r")
    lines = f.readlines()
    f.close()
    return lines

def clean_list(l):
    return ' '.join(l).split()

def make_dict(line):
    global my_dict
    my_dict[line[0]] = {
        "cost": int(line[1]),
        "damage":int(line[2]),
        "armor":int(line[3])
    }
    
def check_win_lose(my_hit_point,boss_hit_point):
    global game_over
    global game_result
    if my_hit_point < 0:
        game_over = True 
        print("Boss Win")
        # game_resultp2.append(cost)
        return True
    if boss_hit_point < 0:
        game_over  = True
        print("Myself Win")
        # game_result.append(cost)
        return True
    
def attack(my_damage,boss_armor, s):
    global boss_hit_point
    global my_hit_point
    attack_hit = my_damage - boss_armor
    if s == 'MY':
        if attack_hit > 0:
            boss_hit_point = boss_hit_point - attack_hit
        else:
            boss_hit_point = boss_hit_point - 1
    if s == 'Boss':
        if attack_hit > 0:
            my_hit_point = my_hit_point - attack_hit
        else:
            my_hit_point = my_hit_point - 1
lines = read_file()
data = read_hit_point_file()
my_dict = {}
for line in lines:
    line = clean_list(line.split("  "))
    if len(line) > 0:
        make_dict(line)
game_result = []
game_resultp2 = []
boss_hit_point = int(data[0].split(':')[1].strip())
boss_damage = int(data[1].split(':')[1].strip())
boss_armor = int(data[2].split(':')[1].strip())
my_hit_point = 100
my_damage = 10
my_armor =  0
game_over = False
while game_over == False:
    attack(my_damage,boss_armor,'MY')
    status = check_win_lose(my_hit_point,boss_hit_point)
    if status :
        break
    attack(boss_damage, my_armor,'Boss')
    status = check_win_lose(my_hit_point,boss_hit_point)
    if status:
        break