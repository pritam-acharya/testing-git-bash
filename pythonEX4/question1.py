# factorial

def fact(x):
    f=1
    for j in range(1,x+1):
        f=f*j
    return f
string='yes'
while(string=='yes'):
    number=int(input("Enter any number to calculate factorial"))
    factorial=fact(number)
    print(f"The factorial of {number} is {factorial}")
    string=input('Do you want to continue, yes or no?')