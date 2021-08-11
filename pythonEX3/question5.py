num = input("Please Enter a Number: ")
num = int(num)
if num==0:
  print(f"{num}!=1")
elif num>0:
  fact = 1
  for i in range(1,num+1):
    fact = fact*i
  print(f"{num}!={fact}")
else :
  print("I dont know what to do with that!")