import math
t = input("Please enter temperature in Fahrenheit or Celsius:")
if(t[-1]=="c" or t[-1]=="C"):
    far = (float(t[0:-1]))*(9/5) + 32
    print(f"The Temperature in Fahrenheit is: {far} F")
elif(t[-1]=="F" or t[-1]=="f"):
    cel = (float(t[0:-1])-32)*(5/9)
    print(f"The Value of the temperature in Celsius is: {cel} C")
else:
    print("Please enter the temperature in the correct format.")