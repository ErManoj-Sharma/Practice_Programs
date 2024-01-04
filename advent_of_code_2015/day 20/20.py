final = 36000000

def get_gift(house_number):
    gift = 0
    i = 1
    while i <= house_number:
        if house_number / i > 0 and house_number % i == 0:
            gift = gift + 10*i
        i = i+1
    return gift

def get_giftp2(house_number):
    gift = 0
    i = 1
    while i <= house_number:
        if house_number < i * 50:
            if house_number / i > 0 and house_number % i == 0:
                gift = gift + 11*i
        i = i+1
    return gift

# Part 1
gift_value = 0
i = 831598
while True:
    if gift_value > final:
        break
    gift = get_gift(i+1)
    gift_value = gift
    i = i + 1
print("Part 1 : ","House Number: ",i, "Gifts: ", gift_value)

# Part 2

gift_value = 0
i = 884518
while True:
    if gift_value > final:
        break
    gift = get_giftp2(i+1)
    gift_value = gift
    i = i + 1
print("Part 1 : ","House Number: ",i, "Gifts: ", gift_value)
