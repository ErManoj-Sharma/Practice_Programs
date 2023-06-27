def read_file(filename):
    result = []
    sub_array = []
    
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            
            if line == '':
                if sub_array:
                    result.append(sub_array)
                    sub_array = []
            else:
                sub_array.append(int(line))
        
        if sub_array:
            result.append(sub_array)
    
    return result


def sum_of_arrays(array):
    return [sum(sub_array) for sub_array in array]

filename = 'day1.txt'
array_2d = read_file(filename)
sum = sum_of_arrays(array_2d)
print(max(sum))
# Answer: 68442

print(sorted(sum)[-1:-4:-1])
# # Answer: [68442, 68218, 68177]
# That's the right answer! You are one gold star closer to collecting enough star fruit.
# You have completed Day 1!