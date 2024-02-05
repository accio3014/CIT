# variable
# variable = value
# Save the value in variable in the format above.
# = Unlike the meaning of the symbol, the value is simply stored in a variable.
# Variable can be whatever you want as long as you follow the rules below.
# 1. Impossible to start with a number
# 2. Special characters are not possible except the symbol “_”
# 3. No spacing
# 4. Reserved words not possible

# name = "cit"
# age = 13
# height = 189
# print(name)
# print(age)
# print(height)


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# Data type(type of value)
# str           String      => " ", ' '
# float         Float       => number with decimal point
# int           Integer     => just number(without decimal point)

# a = "hello"     # str type
# b = 3.14        # float type
# c = 19          # int type


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# output
# print(variable or value)
# Use the above format, output a variable or value, then press Enter.
# Variable or values can be omitted, and if omitted, one blank line is output.
# Multiple outputs are possible using commas(,).

# a = 'cit'
# print(a)
# print()                 # print blank line
# print('cit', 'hello')
# print(3.14)


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# Check the data type
# type(variable or value)   => Get the data type of the variable or value in ()
# print(type(variable or value))
# As in the format above, type() is unconditionally used with print()

# int0 = 1
# float0 = 3.14
# str0 = 'test'
# print(int0, type(int0))
# print(float0, type(float0))
# print(str0, type(str0))


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# Casting
# str(variable or value)     => Convert variable or value to str data type
# float(variable or value)   => Convert variable or value to float data type
# int(variable or value)     => Convert variable or value to int data type
# If used only for calculation, the original value does not convert
# In order to convert the original data type, the value must be put back into the value [ ex. a = int(a) ]

# var1 = 2
# var2 = "31"
# result = var1 + int(var2)   # Save var1 variable + var2 variable converted to int data type in result variable
# print(result)
# print(type(var2))           # Print data type of var2, and the result variable is calculated as an int data type,
#                             # but the data type of the original variable is not converted
# var2 = int(var2)            # Save var2 variable converted to int data type in var2 variable
# print(type(var2))           # Print data type of var2


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# input
# input(string or varialbe or value)
# After outputting a string or variable or value, keyboard input is received unitl the Enter key pressed.
# variable = input(string or varialbe or value)
# The above format is mainly used, if only input() is used, the input value cannot be saved.
# input() always stroes the value as str data type.

# var1 = 2            
# var2 = input("Insert anything : ")  
# print(var2) 
# print(type(var2))   


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# print("Hello. Enter your name.")
# name = input()

# print("Welcome.", name, ", Enter your age.")
# age = input()
# age = int(age)
# year = 2024 - age

# print("You were born in", year, "Enter your height.")
# height = input()
# height = int(height)

# two_m = 200 - height
# print("There are", two_m, "cm left unitl 2m.")





