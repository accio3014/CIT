# list
# variable = ["value", value]       => The data type of the value does not matter
# Use in the above form
# List is a collection of multiple data types in order in one variable.
# The order of values starts from 0 => It is called the index number.
# When bringing in list values, refer to them using []

# list1 = [1, 'cit', True]
# print(list1)
# print(list1[0])     # Get list1 index number 0 value.
# print(list1[2])
# print(list1[3])     # Get list1 index number 0 value. There is index number 3, so an error occurs


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# You can use the index number to modify the value at that index number.
# Changing the value can be done as if saving the value in a variable.
# a = [1, 'cit', True]
# print(a)

# a[1] = "hello"  # Change the value of the index number 1 of a.
# print(a)


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# list1 = ["abc", "dfg", "hij", 123, 456 ]
# print(list1)
# print()

# print("Q1. Change the 1st element of list1 to 'park'.")
# list1[1] = 'park'
# print(list1)
# print()




# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# for i in range(1, 9, 2):
#     print(i)

# list1 = [1, 3, 5, 7]
# for i in list1:         # Can insert a list variable instead of range() in for loop.
#     print(i)            # Get the elements of a list one by one


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

name = ["Kim", "Gu", "Koo", "Seong"]
score = [92, 96, 98, 100]

add_score = 92 + 96 + score[2] + 100
print(add_score)



# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# List function
# listName.insert(Index number, Value to add)
# insert() add one value to index number. If there is a value that index, the values are pushed back.
# If index number is out of range, the value is insert to the end.

# listName.append(Value to add)
# appened() add one value append to the end.

# del(listName[Index number])
# In the case of del(), the value at the index number of the list deleted, 
# and if there is an index number after it, it is pulled forward.
# If index number is out of range, an error occurs.

# listName.remove(Value to remove)
# In the case of remove(), the value to be deleted is found in the list and deleted.
# If there is an index number after it, it is pulled forward.
# If the value to be deleted is not in the list, an error occurs.

# listName.index(Value to find index)
# In the case of index(), the index number where the value is located is returned.
# If the value to find is not in the list, an error occurs.
# If there are multiple values in the list, the number with the lowest index is returend.

# len(listName)
# In the case of len(), the length of the listName is returned.
# (It is different from the index, the last number of the index is the value -1 of len(listName))

# sum(listName)
# In the case of sum(), it returns after adding all the values in the listName. 
# (Available only when the list data types are numeric.)
# If the data types in the list are mixed with str and numbers, an error occurs

# listName.count(Value to counter)
# In the case of count(), it returns how many values are in the list.
# 0 if the value to be counted is not in list.

# listName.sort()
# Sort the contents of the list in ascending order.