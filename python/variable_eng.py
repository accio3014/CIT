# variable
# variable = value
# Save the value in variable in the format above.

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


# int1 = 2
# int2 =31
# str1 = "car"
# str2 = "car2"

# print(int1)
# print(type(int1))       # check for int1 data type
# print(int2)
# print(type(int2))       # check for int2 data type
# print(str1)
# print(type(str1))       # check for str1 data type
# print(str2)
# print(type(str2))       # check for str2 data type


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# Casting
# int(variable or value)     => Convert variable or value to int data type
# str(variable or value)     => Convert variable or value to str data type
# float(variable or value)   => Convert variable or value to float data type
# If used only for calculation, the original value does not convert
# In order to convert the original data type, the value must be put back into the value [ ex. a = int(a) ]

# var1 = 2
# var2 = '31'
# result = var1 + int(var2)   # Save var1 variable + var2 variable converted to int data type in result variable
# print(result)
# print(type(var2))           # Print data type of var2, and the result variable is calculated as an int data type,
#                             # but the data type of the original variable is not converted
# var2 = int(var2)            # Save var2 variable converted to int data type in var2 variable
# print(type(var2))           # Print data type of var2


print("This program was created to introduce myself.")
name = "My name is Hong Gil Dong"
print(name)
print()
print("And my school is YISS!")
