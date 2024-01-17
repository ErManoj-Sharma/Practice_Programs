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

def update_mana_turns():
    global mana_turns
    global player_mana
    mana_turns = mana_turns - 1
    player_mana = player_mana + 101
    print(f"Recharge provides 101 mana; its timer is now {mana_turns}.")
    if mana_turns == 0:
        print(f"Recharge wears off.")

def update_armor_turns_player():
    global armor_turns 
    armor_turns = armor_turns - 1
    print(f"Shield's timer is now {armor_turns}")
    if armor_turns == 0:
        print(f"Shield wears off, decreasing armor by 7.")
        player_armor = player_armor - 7

def update_damage_turns_player():
    global damage_turns 
    global boss_hit_point
    damage_turns = damage_turns - 1
    boss_hit_point = boss_hit_point - 3
    print(f"Poison deals 3 damage; its timer is now {damage_turns}.")
    if damage_turns == 0:
        print("Damage wears off.")

def attack(s):
    global player_hit_point
    global player_armor
    global player_mana
    global boss_hit_point
    global mana_turns 
    global armor_turns 
    global damage_turns 
    if s == "MY":
        print("-- Player Turn --")
        print(f"-- Player has {player_hit_point} hit points, {player_armor} armor, {player_mana} mana")
        print(f"-- Boss has {boss_hit_point} hit points")
        if mana_turns > 0 :
            update_mana_turns(mana_turns,player_mana)
        if armor_turns > 0:
            update_armor_turns_player()
        if damage_turns > 0:
            update_damage_turns_player()
            pass


my_dict = {
    "Magic Missile":{ "cost":53, "damage": 4,},
    "Drain":{"cost":73, "damage":2, "heal":2},
    "Shield":{"cost":113, "turns":6, "armor":7},
    "Poison":{"cost":173, "turns":6, "damage":3},
    "Recharge":{"cost":229,"turns":5,"mana":101}
}
data = read_hit_point_file()
print(data)
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
    break
print("Game End")