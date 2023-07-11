def read_file(filename):
    with open(filename, "r") as file:
        list1 = []
        lines = file.readlines()  # Read all lines into a list
        list1 = [list(i) for i in [i.strip() for i in lines]]
    return list1


def print_list(list1):
    for i in list1:
        print(i, end='\n')


# def part1_top_list_max(start, j, list1):
#     top_list = []
#     for i in range(start-1, -1, -1):
#         top_list.append(list1[i][j])
#     return (max(top_list))


# def part1_bottom_list_max(start, j, list1):
#     bottom_list = []
#     for i in range(start+1, len(list1)):
#         bottom_list.append(list1[i][j])
#     return (max(bottom_list))


# def part1_left_list_max(start, i, list1):
#     left_list = []
#     for j in range(start-1, -1, -1):
#         left_list.append(list1[i][j])
#     return (max(left_list))


# def part1_right_list_max(start, i, list1):
#     right_list = []
#     for j in range(start+1, len(list1)):
#         right_list.append(list1[i][j])
#     return (max(right_list))


list1 = read_file('day8.txt')
rows = len(list1[0])
colm = len(list1)
total = (2 * rows) + (2 * colm) - 4


# for i in range(1, len(list1)-1):
#     for j in range(1, len(list1[i])-1):
#         item = list1[i][j]
#         top = part1_top_list_max(i, j, list1)
#         bottom = part1_bottom_list_max(i, j, list1)
#         left = part1_left_list_max(j, i, list1)
#         right = part1_right_list_max(j, i, list1)

#         if (top < item or bottom < item or left < item or right < item):
#             total = total+1

# print("Part 1 : ",total)

def part2_top_list_max(start, j, list1):
    top_list = []
    print("item is : ", list1[start][j])
    for i in range(start-1, -1, -1):
        if (list1[i][j] < list1[start][j]):
            top_list.append(list1[i][j])
    return (len(top_list))


def part2_bottom_list_max(start, j, list1):
    bottom_list = []
    for i in range(start+1, len(list1)):
        if (list1[i][j] < list1[start][j]):
            bottom_list.append(list1[i][j])
    return (len(bottom_list))


def part2_left_list_max(start, i, list1):
    left_list = []
    for j in range(start-1, -1, -1):
        if (list1[i][j] < list1[start][j]):
            left_list.append(list1[i][j])
        if (list1[i][j] == list1[start][j]):
            left_list.append(list1[i][j])
            return (len(left_list))
    return (len(left_list))


def part2_right_list_max(start, i, list1):
    right_list = []
    for j in range(start+1, len(list1)):
        if (list1[i][j] < list1[i][start]):
            print(list1[i][j])
            right_list.append(list1[i][j])
    print(right_list)
    return (len(right_list))


# Part 2
list_max = []
for i in range(1, len(list1)-1):
    for j in range(1, len(list1[i])-1):
        item = list1[i][j]
        top = part2_top_list_max(i, j, list1)
        bottom = part2_bottom_list_max(i, j, list1)
        left = part2_left_list_max(j, i, list1)
        right = part2_right_list_max(j, i, list1)
        print("top: ", top,"\n","left : ",left, "right : ",right,"bottom: ",bottom,"\n",
               "\n")
        number = top * bottom * left * right
        list_max.append(number)
        print('\n')
    # break

print(list_max)
print(max(list_max))

#172224