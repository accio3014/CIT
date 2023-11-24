import math

x = 121
str_x = str(x)
x_len = len(str_x)
for i in range(0, math.ceil(x_len / 2), 1):
    if(i >= math.ceil(x_len / 2)):
        print(True)
    
    if(str_x[i] == str_x[-i-1]):
        continue
    else:
        print('false')