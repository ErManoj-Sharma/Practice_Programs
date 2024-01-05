from itertools import product
l1 = ['Dagger', 'Shortsword', 'Warhammer', 'Longsword', 'Greataxe']
l2 = ['NoArmor', 'Leather', 'Chainmail', 'Splintmail', 'Bandedmail', 'Platemail']
l3 = ['NoRing', 'Damage+1', 'Damage+2', 'Damage+3', 'Defense+1', 'Defense+2', 'Defense+3']
l4 = ['NoRing', 'Damage+1', 'Damage+2', 'Damage+3', 'Defense+1', 'Defense+2', 'Defense+3']

def clean_list(l):
    return ' '.join(l).split()

def read_file():
    f = open("input.txt", "r")
    lines = f.readlines()
    f.close()
    return lines

def make_dict(line):
    global my_dict
    my_dict[line[0]] = {
        "cost": int(line[1]),
        "damage":int(line[2]),
        "armor":int(line[3])
    }

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

def check_win_lose(my_hit_point,boss_hit_point, cost,p):
    global game_over
    global game_result
    if my_hit_point <= 0:
        game_over = True 
        return True
    if boss_hit_point <= 0:
        game_over  = True
        game_result.append([cost,p])
        return True

lines = read_file()

my_dict = {}
for line in lines:
    line = clean_list(line.split("  "))
    if len(line) > 0:
        make_dict(line)
all_permutations = list(product(l1, l2, l3, l4))
game_result = []
for p in all_permutations:
    boss_hit_point = 103
    boss_damage = 9
    boss_armor = 2

    my_hit_point = 100
    cost= 0
    damage =0
    armor = 0
    for i in range(0,4):
       cost = cost +  int(my_dict[list(p)[i]]["cost"])
       damage = damage + int(my_dict[list(p)[i]]["damage"])
       armor = armor + int(my_dict[list(p)[i]]["armor"])
    my_cost = cost
    my_damage = damage
    my_armor = armor 
    game_over = False
    while game_over == False:
        attack(my_damage,boss_armor,'MY')
        status = check_win_lose(my_hit_point,boss_hit_point, my_cost,p)
        if status :
            break
        attack(boss_damage, my_armor,'Boss')
        status = check_win_lose(my_hit_point,boss_hit_point, my_cost,p)
        if status:
            break
m = 1000
a = ''
for game in game_result:
    if game[0] < m:
        m = game[0]
        a = game[1]
print(m,a)

