# -------------------------------------------------------
# part (a)
import math
vi = input("Please enter initial velocity in meters per second")
angl = input("Please enter the angle the projectile makes with the horizontal (in degrees)")
g = 9.8
theta = float(angl)*(math.pi/180)   # note the conversion from int to float
float(theta)
MaxHt = (float(vi)*math.sin(theta)**2)/(2*g)
TimeForMaxHt = (float(vi)*math.sin(theta)) / g
print(f"The maximum height attained is {MaxHt} mtrs and the Time take to reach that is {TimeForMaxHt} seconds.")
# --------------------------------------------------------
# part (b)
MaxRng = (float(vi)**2) * math.sin(2*theta) / g
print(f"The maximum horizontal distance travelled is {MaxRng} meters.")
# ---------------------------------------------------------
# part (c)
TimeFlight = 2*TimeForMaxHt
vy = float(vi)*math.sin(theta)   # y component of velocity
ay = -0.5*g   # y component of acceleration due to gravity
t1 = ((float(vy)) + math.sqrt((float(vy))**2-2*g*MaxHt))/g
t2 = (float(vy) - math.sqrt((float(vy))**2 - 2*g*MaxHt))/g
print(f"The total time of flight is {TimeFlight} seconds and the time(s) at which 80% of maximum height is reached is {t1} seconds and {t2} seconds")
# -----------------------------------------------------------

