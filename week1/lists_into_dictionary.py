'''

Write a python program to merge two lists into a dict

Example
                 fruits = ['oranges', 'apples','peaches']
                 quantity = [12,14,15]
                 result = {'oranges':12,'apples':14,'peaches':15}


'''


#List of fruits
fruits = ['oranges','apples','peaches']

#List of quantities
quantity = [12,14,15]

#Create an Empty Fruit Dictionary
fruit_dict = {}

#Create a new variable called index and assign it the value of 0. This variable will hold the position of items in the fruit list
index = 0

#For loop to iterate over the items in the fruit list
for fruit in fruits :
    '''Create a new key in the fruit_dict by the name of the fruit and assign the corresponding item from the quantity list
     - This will be done for each iteration of the loop
     '''
    fruit_dict[fruit] = quantity[index]
    #increment the index value by 1, the new index will be 1 plus the previous index
    index = index + 1

#Print the fruit dictionary
print fruit_dict