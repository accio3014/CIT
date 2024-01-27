# reference.py

# 1. Formatting
# 2. Escape Code
# 3. Ignore line breaks


# [1. Formatting]

# Formatting    => Formatting symbols must be write inside " " symbol.
# Why use it?
# If print a variable or value using the , symbol inside print(), a space is automatically created, 
# and the symbol cannot be used indefinitely.

# Hello CIT     <= Want to print it like this
# a = "Hello"
# b = "CIT"
# print(a,b)                  # If you use the , symbol, a space is automatically created, 
#                             # so you need to calculate the space when printing.
# print("%s %s" % (a, b))     # When formatting is used, the variable value is placed where I want it to be.


# Formatting symbols : write inside " "
# str       => %s
# float     => %f
# int       => %d
# The above formatting symbols are used according to the data type of the variable.

# 1. When print one variable
# print("%f" % (variable))                      Value of variable enters the %f position.
# 2. When print two or more variable
# print("%f %s" % (variable A, variable B))     Value of variable A enters the %f position, 
#                                               Value of variable B enters the %s position.

# My name is Park! And my age is 15. <= Want to print it like this
# name = "Park"   # %s, because str
# print("My name is %s! And my age is 15." % (name))

# i = "My"        # %s, because str
# print("%s name is %s! And my age is 15." % (i, name))

# age = 15        # %d, because integer
# print("%s name is %s! And my age is %d." % (i, name, age))

# print("%d %d" % (age, age)) # The same variable can be used multiple times


# 포맷팅의 소수점 표시
# 실수의 경우 %f를 사용
# %f 사용시 기본 값은 소수점 6번째 자리 수 까지 출력. 정확히는 7번째 자리에서 반올림한 후 6자리 까지 출력
# pi = 3.1415
# print("%f" % (pi))  # 만약 변수 값이 6자리 보다 작으면 나머지 소수점 자리의 숫자는 0으로 출력

# %.숫자f       => 소수점 숫자 번째 까지 출력. 정확히는 숫자 + 1 자리수에서 반올림한 후 숫자 번째 자리수까지 출력
# print("%.3f" % (pi))    # 소수점 4번째 자리에서 반올림 한 후 소수점 3째 자리까지 출력



# 포매팅을 이용해서 문자열을 정렬할 수 있다.
# 100000
#  10000
#   1000
# 위 와 같이 출력하고 싶을 경우
# a = 100000
# b = 10000
# c = 1000
# print("%7d" % a)
# print("%7d" % b)
# print("%7d" % c)

# 포매팅 기호 사이에 숫자를 넣을 수 있음
# %7d   =>  7칸의 공간에서 출력할 값을 오른쪽에 붙여 출력
# %-7d  =>  7칸의 공간에서 출력할 값을 왼쪽에 붙여 출력
# 만약 출력할 내용이 7칸보다 클경우 왼쪽에 붙여 출력
# c = 1000
# print('%7d' % c)
# print('%-7dhi' % c)

# 위와 같이 정렬에 대한 것은 %s, %d, %f 전부 가능
# %f에만 있는 특별한 것이 있다.
# 만약에 소수점 3자리까지 출력을 하고 싶다  => %.3f
# 정확히는 4자리에 반올림 한 후 3자리 까지 출력
# pi = 3.14159265
# print('%5.3f' % pi)      # 3.142가 출력된 이유는 4번째 자리의 값이 5이므로 반올림


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# [2. Escape Code]
# 특별한 문자로 문자 출력시에 사용한다  => 따음표 기호('') 안에 있음
# \n    문자열 안에서 줄을 바꿀 때 사용
# \t    문자열 사이에 탭 간격을 줄 때 사용
# \\    문자 \를 그대로 표현할 때 사용
# \'    ' 를 출력
# \"    " 를 출력
# print("Hello\nCIT")     # \n 사용
# print("Hello\tCIT")     # \t 사용
# print("Hello\\CIT")     # \\ 사용
# print("\' \"")



# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# [3. Ignore line breaks]
# print()를 사용하게 되면 자동으로 줄을 바꾼다
# 이것을 무시하기 위해서는 print() 안에 ,end=''을 사용한다.
# 정확한 ,end='문자'의 뜻은 어떤 내용을 출력하고 뒤에 줄 바꿈을 하지 않는 후
# 문자를 추가한다. 보통 빈칸으로 많이 사용
# for i in range(5):
#     print('%d ' % i, end='')    # 한줄에 반복한 결과 출력
# print()

# for i in range(5):
#     print('%d ' % i)    # 한줄에 반복한 결과 출력
# print()