n="yes"
def prime(x):
    k=0
    for i in range(2, x):
        if x % i == 0:
            k = k + 1
    if(k==0):
        return 1
    else:
        return 0
while n=="yes":

    x=int(input("Enter any number"))
    if(prime(x)):
        print('True')
    else:
        print('False')
    n=input("Do you want to enter once again")