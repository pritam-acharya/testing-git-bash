frnds = []
while len(frnds)<=12:
    FrNm = input("Please enter the name(s) of your friend(s) [Once you are done, type Complete]: ")
    if FrNm == 'Complete' or FrNm == " ":
        break
    else:
        frnds.append(FrNm)
if len(frnds)<3:
    print(f"Team 1: {frnds[0]}")
    print(f"Team 2: {frnds[1]}")
    print("Team 3: Please make more friends.")
else:
    totfren = len(frnds)
    Team1 = frnds[0::3]    # defining team but slicing the frnds list with a step of '3'.
    Team2 = frnds[2::3]
    Team3 = frnds[1::3]
    print(f"You entered the names of {totfren} people, the teams are as follows:")
    print(f"Team1: {Team1}")
    print(f"Team2: {Team2}")
    print(f"Team3: {Team3}")
print("Thank you for using our services.")