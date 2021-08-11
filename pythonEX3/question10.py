vector1 = []
vector2 = []
string = int(input("Press '1' for Dot-Product and '2' for Cross-Product of Two Vectors in R^3"))
if string == 1:
    print("Enter the components of vector 1")
    for i in range(0,3):
        vector1.append(float(input(" ")))
    print("Enter components of vector 2")
    for j in range(0,3):
        vector2.append(float(input(" ")))
    dotproduct = 0
    for i in range(0,3):
        dotproduct = dotproduct+(vector1[i]*vector2[i])
    print(f"The Dot Product is {dotproduct}")
elif string == 2:
    print("Enter the components of vector 1")
    for i in range(0, 3):
        vector1.append(float(input(" ")))
    print("Enter components of vector 2")
    for j in range(0, 3):
        vector2.append(float(input(" ")))
    cross = [0,0,0]
    cross[0] = cross[0]+(vector1[1]*vector2[2])-(vector1[2]*vector2[1])
    cross[1] = cross[1]-(vector1[0]*vector2[2])+(vector1[2]*vector2[0])
    cross[2] = cross[2]+(vector1[0]*vector2[1])-(vector1[1]*vector2[0])
    print(f"The Cross Product of the Vectors is {cross}")
else:
    print("Please enter Valid Values.")