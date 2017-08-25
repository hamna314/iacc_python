#define the function fib
def fib(n):
   if n <= 1:
       return n
   else:
       #call the function fib recursively to calculate sum of the previous 2 numbers
       return(fib(n-1) + fib(n-2))



#Get input from the user
num_in_seq = raw_input('How many fibonacci numbers do you want ..? >>> ')

#Initialize an empty list to hold numbers from the finonacci sequence
fibonacci_list = []

#Iterate over the numbers in sequence
for i in range(int(num_in_seq)):

    #add the result of each number to the list
    fibonacci_list.append(fib(i))

#print the final list
print fibonacci_list
