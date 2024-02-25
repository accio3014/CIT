# if_eng.py

# Comparison operators
# The result of the comparison operation is always True or False.
# ==    : True if the same, False if different.
# !=    : True if different, False if the same
# <
# >
# <=
# >=

# print(5 != 2)
# print(5 < 2)


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# if(condition) :
#   Run if the above condition is True.
# elif(condition) :
#   Run if the above condition is True.
# else :
#   Run if all condition are False.

# if    : always use 1
# elif  : use range 0 ~ infinity
# else  : use 0 or 1
# if can be used by nesting within if.


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# 100 ~ 90  : A
# 89 ~ 70   : B
# 69 ~ 60   : C
# 59 ~      : D

# score = int(input())

# if(100 >= score >= 90) :
#     print('A')
# elif(89 >= score >= 70):
#     print('B')
# elif(69 >= score >= 60):
#     print('C')
# elif(59 >= score >= 0):
#     print('D')

# print("End")


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# age = int(input("Enter your age : "))

# if(age >= 12) :
#     print("Good, Have fun watching.")
# else :
#     print("Sorry, Only over 12 years watch the movie.")


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# print("Enter number.")
# num = int(input())

# if(num % 2 == 0) :
#     print("Even.")
# else :
#     print("Odd")


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# and   : True if both sides are True, False if even one side is False
# or    : False if both sides are False, True if at least one side is True
# not   : If True, the result is reversed to Flase. If it is Flase, the result is reversed to True.
# The execution order is executed in the order of not, and, or.


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# An year is said to be leap year if it divisible by 4 and not divisible by 100, with an exception that it is divisible by 400.
# year = int(input('Enter year : '))
 
# if((year%4 == 0) and (year%100 != 0)) or (year%400 == 0) :
#     print(year, "is a leap year.")
# else :
#     print(year, "is not a leap year.")