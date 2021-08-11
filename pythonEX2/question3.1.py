# question 3 part (d)
from math import*
print("We will be working with the velocities of 10m/s, 50 m/s, and 100 m/s. Please press Return to choose and angle of your choice")
angl = input("Please enter the angle the projectile makes with the horizontal (in degrees)")
g = 9.8
theta = float(angl)*(pi/180)   # note the conversion from int to float
float(theta)
v1 = 10.0
v2 = 50.0
v3 = 100.0
MaxHt1 = (float(v1)*sin(theta)**2)/(2*g)
TimeForMaxHt1 = (float(v1)*sin(theta)) / g
TimeFlight1 = 2*TimeForMaxHt1
MaxHt2 = (float(v2)*sin(theta)**2)/(2*g)
TimeForMaxHt2 = (float(v2)*sin(theta)) / g
TimeFlight2 = 2*TimeForMaxHt2
MaxHt3 = (float(v3)*sin(theta)**2)/(2*g)
TimeForMaxHt3 = (float(v3)*sin(theta)) / g
TimeFlight3 = 2*TimeForMaxHt3
print(f"|   Velocity   | Time of Flight (sec) |   Height (mtrs)   |")
print(f"|---------------------------------------------------------|")
print(f"|      10     |       {TimeFlight1:.4f}       |      {MaxHt1:.4f}     |")
print(f"|      50     |       {TimeFlight2:.4f}       |      {MaxHt2:.4f}     |")
print(f"|     100     |       {TimeFlight3:.4f}       |      {MaxHt3:.4f}     |")
print(f"|---------------------------------------------------------|")


