from itertools import permutations
def read_file():
    f = open("input.txt", "r")
    lines = f.readlines()
    f.close()
    return lines

def calculate_total_distance(path, distances):
    total_distance = 0
    for i in range(len(path) - 1):
        city1, city2 = path[i], path[i + 1]
        total_distance += int(distances[(city1, city2)])
    return total_distance

def traveling_salesman_bruteforce(a):
    cities = set()
    distances = {}
    
    # Extract cities and distances from input
    for route in a:
        city1, city2, distance = route
        cities.add(city1)
        cities.add(city2)
        distances[(city1, city2)] = distance
    
    # Generate all possible permutations of cities
    all_permutations = permutations(cities)
    
    # Initialize variables for the best solution
    best_path = None
    longest_path = None
    min_distance = float('inf')
    max_distance = float('-inf')

    
    # Iterate through all permutations and find the minimum distance
    for path in all_permutations:
        total_distance = calculate_total_distance(path, distances)
        if total_distance < min_distance:
            min_distance = total_distance
            best_path = path
        if total_distance > max_distance:
            max_distance = total_distance
            longest_path = path
    
    return best_path, min_distance ,max_distance, longest_path

lines = read_file()
distance_list = []
for line in lines:
    line = line.strip()
    source = line.split('to')[0].strip()
    destination = line.split('to')[1].split('=')[0].strip()
    distance = line.split('to')[1].split('=')[1].strip()
    distance_list.append([source, destination, distance])
    distance_list.append([ destination, source, distance])

best_path, min_distance, max_distance, longest_path = traveling_salesman_bruteforce(distance_list)
print("Part 1: ",best_path, min_distance)
print("Part 2: ",longest_path,max_distance)