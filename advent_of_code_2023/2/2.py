def read_file():
    f = open("input.txt", "r")
    lines = f.readlines()
    f.close()
    return lines

def make_dict(l, index):
    global my_dict
    print("Index: ",index, " List: ", l)
    # length = int(len(l))
    # # print(length)
    # for i in range(0,1):
    #     arr = l[i].split(',')
    #     arr_len = len(arr)
    #     print(arr)
    #     # print(arr_len)
    #     for i in range(0,arr_len):
    #         if arr[i].strip().split(' ')[1] == 'red':
    #             arr[i].strip().split(' ')[0]
    #         if arr[i].strip().split(' ')[1] == 'blue':
    #             arr[i].strip().split(' ')[0]
    #         if arr[i].strip().split(' ')[1] == 'green':
    #             arr[i].strip().split(' ')[0]

green_ball = 13
blue_ball = 14
red_ball = 12
my_dict = {} 
lines_array = read_file()
i = 0
for line in lines_array:
    i = i+1
    # print(line[8:].split(";"))
    make_dict(line[8:].split(";"), i)
