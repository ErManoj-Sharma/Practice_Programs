import itertools
from itertools import product
def read_file():
    f = open("input.txt", "r")
    lines = f.readlines()
    f.close()
    return list(line.replace("\n",'') for line in lines)

def evaluate_left_to_right(expression):
    tokens = expression.split()
    result = int(tokens[0])
    
    for i in range(1, len(tokens), 2):
        operator = tokens[i]
        number = int(tokens[i + 1])
        
        if operator == '+':
            result += number
        elif operator == '*':
            result *= number
        else:
            raise ValueError(f"Unsupported operator: {operator}")
    
    return result

def check_valid_equation(eqn):
    ans, exp = int(eqn[0]), eqn[1].strip()
    exp = exp.split(" ")
    operator_combinations = itertools.product(operators, repeat=len(exp)-1)
    for ops in operator_combinations:
        expression = f"{exp[0]}"
        for i, op in enumerate(ops):
            expression += f" {op} {exp[i+1]}" 
        
        if evaluate_left_to_right(expression) == ans:
            return ans
    return False

lines = read_file()
equations = []
for line in lines:
    equations.append(line.split(":"))

lst=[]
operators = ['+', '*']
for equation in equations:
    if check_valid_equation(equation):
        lst.append(int(equation[0]))
print("Part 1 ",sum(lst))

# Part 2 
lines = read_file()
equations = []
size = 0
for line in lines:
    exps = line.strip().split()
    equations.append((int(exps[0][:-1]), [int(i) for i in exps[1:]]))
    size = max(size, len(exps)-1)

valid = ('+', '*', '|')
answer = 0
for target, digits in equations:  #.items():
    for ops in product(valid, repeat=len(digits)-1):
        val = digits[0]
        for op, i in zip(ops, digits[1:]):
            if op == '+':
                val += i
            elif op == '*':
                val *= i
            else:
                val = int(str(val) + str(i))
        
        if val == target:
            answer += target
            break
print("Part 2: ", answer)
