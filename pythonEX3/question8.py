def average(x):
    sum = 0
    for i in range(0,n):
        sum=sum+x[i]
    return (sum/n)
def sd(x):
    sum1=0
    for i in range(0,n):
        sum1=sum1+pow(x[i]-average(x),2)
    return (pow(sum1/n,0.5))
list = []
n = int(input("How many entries?"))
for i in range(0,n):
    list.append(float(input(" ")))
print(f"Mean of the Entries is {average(list)}")
print(f"Std Dev of the numbers are {sd(list)}")