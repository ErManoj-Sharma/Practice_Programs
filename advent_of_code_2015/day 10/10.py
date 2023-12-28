def read_file():
    f = open("input.txt", "r")
    lines = f.readline()
    f.close()
    return lines

# count and Say game
# Part 2 : https://www.youtube.com/watch?v=ea7lJkEhytA
def count_and_say(n):
    global line
    if n == 1:
        return str(line)

    prev_sequence = count_and_say(n - 1)
    result = ''
    count = 1

    for i in range(1, len(prev_sequence)):
        if prev_sequence[i] == prev_sequence[i - 1]:
            count += 1
        else:
            result += str(count) + prev_sequence[i - 1]
            count = 1

    result += str(count) + prev_sequence[-1]

    return result

line = read_file()
# Part 1
op = count_and_say(41)
print("Part 1: ",len(op))

# Part 2
op = count_and_say(51)
print("Part 2: ",len(op))