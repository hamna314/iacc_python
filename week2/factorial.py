# Write a program to calculate the factorial of a given number ( use recursion )
#Factorial of n is n * (n-1) * (n-2) ... 1, which in other words is n * (n-1)!  or n multiplied by (n-1) factorial
#example Factorial of 5 :  5 * 4 * 3 * 2 * 1 = 120


#Define a function called factorial
def factorial(n):
    #If Number passed is 0, return 1
    if n == 0:
        return 1
    else:
        #Take the number and multiply it by factorial of (n-1)
        return n * factorial(n-1)


#Get the input frome the user
num = raw_input('Enter a Number >>>> ')


#Print the response after calling teh function
print 'Factorial of the number ', num, ' is ', factorial(int(num))