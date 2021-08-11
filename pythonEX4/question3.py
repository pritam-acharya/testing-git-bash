# sine
x=float(input("Enter number of choice"))
i=float(input("Enter which term to to be calculated "))
n=float(input(f"Enter {i-1}th term"))
new=((pow(-1,i))*pow(x,2)*n)/(4*i*i+2*i)
print(f'{new} is the {i}th term in the sine expansion of {x}')

# cosine
x=float(input("Enter number of choice"))
i=float(input("Enter which term to to be calculated "))
n=float(input(f"Enter {i-1}th term"))
new=((-1*pow(x,2)*n)/(i*i-i))
print(f'{new} is the {i}th term in the cosine expansion of {x}')