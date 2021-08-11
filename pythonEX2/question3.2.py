# question 3 part (e)
import  math
v1 = 10.0
v2 = 100.0
alphvalues = range(0,90,1) # alphavalues refer to the value of the angle made by the projectile in degrees.
g = 9.8
anglVal1 = []
rangeVal1 = []
for angl in alphvalues:
    anglrad = math.radians(angl)
    MaxRng = (float(v1) ** 2) * math.sin(2 * anglrad) / g
    anglVal1.append(angl) # The append() method adds a single item to the existing list.
    rangeVal1.append(MaxRng)
MaxiRng = max(rangeVal1)
MaxRangePos = rangeVal1.index(MaxiRng)
MaxRngAngl = anglVal1[MaxRangePos]
print(f"The Maximum Range for 10.0 m/s is {MaxiRng:.3f} m, at {MaxRngAngl} degrees.")
anglVal2 = []
rangeVal2 = []
for angl in alphvalues:
    anglrad = math.radians(angl)
    MaxRng = (float(v2) ** 2) * math.sin(2 * anglrad) / g
    anglVal2.append(angl) # The append() method adds a single item to the existing list.
    rangeVal2.append(MaxRng)
MaxiRng = max(rangeVal2)
MaxRangePos = rangeVal2.index(MaxiRng)
MaxRngAngl = anglVal2[MaxRangePos]
print(f"The Maximum Range for 100.0 m/s is {MaxiRng:.3f} m, at {MaxRngAngl} degrees.")