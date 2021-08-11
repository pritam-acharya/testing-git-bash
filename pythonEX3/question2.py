# Python program to check if
# given number is prime or not
num = input("Please enter a Natural Number:")
num = int(num)
if num > 1:
	for i in range(2, int(num)-1):
		if (num % i) == 0:
			print(num, "is not a prime number")
			break
	else:
		print(num, "is a prime number")

else:
	print(num, "is not a prime number, and please don't enter funny stuff.")