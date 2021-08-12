# instead of a program limited to print just the 50 elements,
# i present a program which asks for the number of terms to be printed.
n = int(input("How many terms? "))
# we define the first two terms
n1, n2 = 1, 1
count = 0   # set the initial count to 0
# we first check if the number of terms is valid
if n <= 0:
   print("Please enter a positive integer")
elif n == 1:
   print("Fibonacci sequence uptill",n,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < n:    # count function limits the length of the list to be less than the number of terms entered.
       print(n1)
       nth = n1 + n2
       # now we assign the new updated values to the variable for the recursion to continue.
       n1 = n2
       n2 = nth
       count += 1    # this will keep on increasing the count of the sequence, till the max point of count < n is reached.