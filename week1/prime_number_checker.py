'''
 Write a python program to determine if a given number is a prime number.
 Prime number is only divisible by itself, example 2, 3, 5, 7 etc...
'''

#Create a variable to hold a number which is being evaluated
num = 57;

is_prime = False
i = 2

while num % i !=0 :
    print num, i, num % i
    if i == num - 1:
        is_prime = True
        break
    i = i + 1




print is_prime