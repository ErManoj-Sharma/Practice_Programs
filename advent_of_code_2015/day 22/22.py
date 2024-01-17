def read_hit_point_file():
    f = open("input.txt", "r")
    lines = f.readlines()
    f.close()
    return lines

def check_win_lose(my_hit_point,boss_hit_point):
    global game_over
    if my_hit_point <= 0:
        game_over = True 
        print("Boss Win")
        return True
    if boss_hit_point <= 0:
        game_over  = True
        print("Myself Win")
        return True

def attack(s):
    pass

my_dict = {
    "Magic Missile":{ "cost":53, "damage": 4,},
    "Drain":{"cost":73, "damage":2, "heal":2},
    "Shield":{"cost":113, "turns":6, "armor":7},
    "Poison":{"cost":173, "turns":6, "damage":3},
    "Recharge":{"cost":229,"turns":5,"mana":101}
}
data = read_hit_point_file()

# Boss 
boss_hit_point = int(data[0].split(':')[1].strip())
boss_damage = int(data[1].split(':')[1].strip())
boss_armor = 0

# Player
player_hit_point = 10
player_mana = 250
player_armor = 0

# Turns
mana_turns = 0
armor_turns = 0
damage_turns = 0
game_over = False


while game_over == False:
    attack('MY')
    attack('Boss')