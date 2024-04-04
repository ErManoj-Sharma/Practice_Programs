def read_file():
    f = open("input.txt", "r")
    lines = f.readlines()
    f.close()
    return [line.rstrip() for line in lines ]
def evaluate_expression(expression_string):
    global TOTAL_VALUE
    global DATA_DICT
    print(DATA_DICT)
    expression_array = expression_string.split(' ')
    if len(expression_array) == 1:
        return expression_array[0]
    # if len(expression_array) == 2:
    #     if expression_array[0] == "NOT":
    #         return TOTAL_VALUE - int(DATA_DICT[expression_array[1]])
    # if len(expression_array) == 3:
    #     operator = expression_array[1]
    #     x = expression_array[0]
    #     y = expression_array[2]
    #     if operator == "OR":
    #         return int(DATA_DICT[x]) | int(DATA_DICT[y])
    #     elif operator == "AND":
    #         # print("===============================================")
    #         # print("x: ",x)
    #         # print("y: ",y)
    #         # print(DATA_DICT)
    #         # print(int(DATA_DICT[y]))
    #         # print(int(DATA_DICT[x]) & int(DATA_DICT[y]))
    #         # print("===============================================")

    #         return int(DATA_DICT[x]) & int(DATA_DICT[y])
    #     elif operator == "LSHIFT":
    #         return int(DATA_DICT[x]) << int(y)
    #     elif operator == "RSHIFT":
    #         return int(DATA_DICT[x]) >> int(y)
DATA_DICT = {}
ExpressionString=''
TOTAL_VALUE = 65535
lines = read_file()
for line in lines:
    instruction = line.split('->')
    DATA_DICT[str(instruction[1].strip())] = evaluate_expression(instruction[0].strip())
# print(DATA_DICT, end='\n')
for key, value in DATA_DICT.items():
    if value is not None:
        print(key)