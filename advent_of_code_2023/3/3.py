def read_file():
    f = open("input.txt", "r")
    lines = f.readlines()
    list1 = [list(i) for i in [i.strip() for i in lines]]
    f.close()
    return list1


def fetch_digit(arr, index):
    global l
    start_x = end_x = index
    start_y = None
    end_y = None
    n = 0
    for i in range(0, len(arr)):
        if arr[i].isdigit():
            if i == (len(arr) - 1):
                n = n * 10 + int(arr[i])
                end_y = i
                if n > 0:
                    l.append([n, start_x, start_y, end_x, end_y])
                n = 0
                start_y = None
                end_y = None

            if start_y is None:
                start_y = i

            n = n * 10 + int(arr[i])
        else:
            end_y = i
            if n > 0:
                l.append([n, start_x, start_y, end_x, end_y])
            n = 0
            start_y = None
            end_y = None


def get_neighbors2(matrix, x, y):
    neighbors = []
    rows, cols = len(matrix), len(matrix[0])
    for i in range(-1, 2):
        for j in range(-1, 2):
            new_x, new_y = x + i, y + j
            if 0 <= new_x < rows and 0 <= new_y < cols:
                # Exclude the center element (x, y)
                if (i, j) != (0, 0):
                    if matrix[new_x][new_y] == '*':
                        neighbors.append([new_x+1,new_y+1])
    return neighbors

def get_neighbors(matrix, x, y):
    neighbors = []
    rows, cols = len(matrix), len(matrix[0])

    for i in range(-1, 2):
        for j in range(-1, 2):
            new_x, new_y = x + i, y + j

            # Check if the new coordinates are within the bounds of the matrix
            if 0 <= new_x < rows and 0 <= new_y < cols:
                # Exclude the center element (x, y)
                if (i, j) != (0, 0):
                    neighbors.append(matrix[new_x][new_y])
    return neighbors


def filter_list(arr):
    res = []
    [res.append(x) for x in arr if x not in res and not x.isdigit() and x != "."]
    return res

def find_keys_with_same_values(data):
    value_to_keys = {}
    result = []
    for item in data:
        key, value = list(item.items())[0]
        value = tuple(value[0])  
        if value in value_to_keys:
            result.append([key, value_to_keys[value]])
        else:
            value_to_keys[value] = key
    return result


def filter_empty_values(input_list):
    result = [{list(item.keys())[0]: value} for item in input_list if (value := list(item.values())[0])]
    return result

def check_valid_num(matrix, arr, index):
    global other_list
    start_x = arr[1]
    start_y = arr[2]
    end_x = arr[3]
    end_y = arr[4]
    x_range = range(int(start_x), int(end_x) + 1)  # Adjust the range as needed
    y_range = range(int(start_y), int(end_y))
    all_neighbors1 = []
    all_neighbors2 = []
    seen = set()
    for x in x_range:
        for y in y_range:
            neighbors = get_neighbors(matrix, x, y)
            all_neighbors1.extend(neighbors)

    if len(filter_list(all_neighbors1)) > 0:
        final_list.append(arr[0])

    for x in x_range:
        for y in y_range:
            neighbors = get_neighbors2(matrix, x, y)
            all_neighbors2.extend(neighbors)
    other_list.append({
        arr[0]: [lst for lst in all_neighbors2 if tuple(lst) not in seen and not seen.add(tuple(lst))]
        }
    )


l = []
final_list = []
final_list2 = []
other_list = []
lines = read_file()
for i in range(0, len(lines)):
    fetch_digit(lines[i], i)

for i in range(0, len(l)):
    check_valid_num(lines, l[i], i + 1)
print("Part 1: ", sum(final_list))

op = filter_empty_values(other_list)
res = find_keys_with_same_values(op)
for i in range(len(res)):
    final_list2.append(int(res[i][0]) * int(res[i][1]))

print("Part 2:",sum(final_list2))