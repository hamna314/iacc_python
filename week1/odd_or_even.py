'''
Write a program to determine if a given number say 5 is odd or even

'''

#Create a variable to hold the number 5
num = 5;

'''
Find the remainder when the number is divided by 5 . 
The number is even if it is divisible by 2 or the remainder is 0 and odd if it is not.
Modulus or % is used to calculate the remainder
'''
mod = num % 2;

#If statement to evaluate if the remainder is not 0, which will make the number odd
if mod > 0:
    print num, 'is an odd number';
else:
    print num, 'is an even number';