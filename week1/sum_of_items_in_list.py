'''
Write a python program to sum all the items in a list
'''

#Create a new list with some random numbers
newList = [1,5,19,4,5,8]

#Create a new variable sum_of_List to hold the sum of the items in the list and assign it a value of 0.
sum_of_list = 0

#Create a for loop to iterate over the elements of the list
for item in newList :
    sum_of_list = sum_of_list + item

print sum_of_list

'''
The same thing can be accomplished by using the sum built in function provided by python as demostrated below
'''

# This is an alternate way of calculating the sum of items in the list
print sum(newList)
