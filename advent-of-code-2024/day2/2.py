def read_file():
    f = open("input.txt", "r")
    lines = f.readlines()
    f.close()
    return list(lines)

def is_safe(lst):
    # to convert string to int
    lst = list(map(int,lst))

    if lst == sorted(lst) or lst == sorted(lst, reverse=True):
        for i in range(0, len(lst)-1):
            if not(1 <= abs(lst[i] - lst[i+1]) <= 3):
              return False
        return True
    return False

lines = read_file()
reports = []


for i in range(0,len(lines)):
    reports.append(lines[i].replace("\n",'').split(' '))

safe_count=0
for report in reports:
    if is_safe(report):
        safe_count = safe_count + 1
        # print(report)

print("Safe : ", safe_count)

# Part 2: 

safe_count=0
for report in reports:
    if any(is_safe(report[:i]+ report[i+1:]) for i in range(0,len(report))):
        safe_count = safe_count +1
print(safe_count)

