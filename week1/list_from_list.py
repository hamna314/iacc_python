'''
Given a list of numbers( numList) find all the numbers in the list which are less than 10 and put them in a  new list ( newList )
'''


#New List of some random numbers
numList = [1,12,5,7,8,9,12,4,8];

#New empty list where numbers from numList which are less than 10 are will be copied to
newList = [];

#For loop to iterate over the list
for num in numList:
    #Condition to check if the num or the item in the list is less than 10
    if num < 10:
        print num;
        #If the num is less than 10 add it to the new list
        newList.append(num);
print newList;