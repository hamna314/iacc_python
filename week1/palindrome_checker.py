'''
Write a program to determine if a given word is a palindrome .

Palindrome is a word which reversed is the same as itself. Example :
'''

#Variable to hold the word
word = 'adada'

'''
Convert the word to a list and call it letters.
In the example the word 'abc' when converted to a list will become : ['a','b','c']
'''
letters = list(word)

#Start with the assumption that the word is a palindrome.
is_palindrome = True

#Create a for loop to iterate over the characters of the word in the new letters list
for letter in letters:

    '''
    Check to see if the character is equal to the last character in the list.
    Example : the first letter a is equal to the last letter a 
    '''
    if letter == letters[-1]:
        '''
        If the first letter (a) is equal to the last letter of the list (a in this case), pop the last letter from the list.
        In this example the last letter a will be removed from the list and the new list becomes ['a','b']
        And on the next iteration letter will be b ( the 2nd letter ) which is also the last letter. The loop ends and is_palindrome flag stays true.
        '''
        letters.pop(-1)
    else:
        '''
        If the one of the letters is not equal to the last letter, the execution goes into the else block and is_palindrome will be set to False.
        The keyword break breaks the for loop and stops it from iterating again since we already know the word is not a palindrome 
        and its useless go check other words in the list.
        '''
        is_palindrome = False
        break

print is_palindrome