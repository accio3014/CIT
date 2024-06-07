# for loop

# for variable in range(start, end, step):
#     code to loop

# range(start, end, step) where start, end, step are numbers [ ex. range(1, 5, 2) ]
# From start to end-1(end not included), put the increased/decreased value by step into a variable and loop.
# Don't necessarily have to enter the start and step.
# If start is not entered, 0
# If step is not entered, 1
# range(5)          => start and step not entered
# range(0, 5)       => step not entered
# range(0, 5, 1)    => standard


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# for i in range(0, 5, 1) :
#     print(i)


# for j in range(0, 5, 1) :
#     print("Hello")


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# while

# while(condition) :
#   code...

# Use the above format
# Similar to an if, run code when the codition is True.

# x = 1
# while(x <= 5):
#     print(x)
#     x = x + 1


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# x = 1
# while(x <= 5):
#     print(x)
#     x = x +2

# i = 2
# while(i <= 100):
#     print(i)
#     i = i + 2


# j = 7
# while(j <= 100):
#     print(j)
#     j = j + 7


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# infinite loop, break, continue

# infinite loop in while loop.
# while(True) :
#   code...
# Use the above format.


# break
# The moment continue is encountered, loop is end.
# i = 0
# while(True) :
#     print(i)
#     if(i == 10) :
#         break
#     i += 1          # i = i + 1


# continue
# The moment continue is encountered, run the next loop.
# for i in range(0, 10, 1) :
#     if(i%2 == 0) :
#         continue        # If it is an even number, go to the next loop(even numbers are not print)
#     print(i)


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# Nested loop
# Format with a loop inside a loop
# If the loop is nested twice, it is a double loop, and if it is nested three times, it is a triple loop.
# for x in range(1, 10, 1) :          # repeat a total of 9 times
# 	for y in range(1, 10, 1) :      # repeat 81 times in total
# 		print(x, "*", y, "=", x*y)


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# x = 1
# while(x <= 9) :
#     y = 1
#     while(y <= 9) :
#         print(x, "*", y, "=", x*y)
#         y = y + 1
#     x = x + 1


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# for x in range(1, 10, 1) :
# 	for y in range(1, x+1, 1) :
# 		print(x, "*", y, "=", x*y)


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #