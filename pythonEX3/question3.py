roll = input("Please enter your IISER Roll Number:")
if len(roll) == 8 and float(roll[0:4]) < 2021 and int(roll[5:]) < 500:
    if float(roll[0:4]) < 2006:
        print("Bruh! IISER Pune was established in 2006. Please enter a valid roll number.")
    elif int(roll[4]) == 1:
        print(f"You are enrolled in the BSMS Program and you will graduate in the year {int(roll[0:4])+5}.")
    elif int(roll[4]) == 2:
        print(f"You are an iPhD student and you will graduate in the year {int(roll[0:4])+6}.")
    elif int(roll[4]) == 3:
        print(f"You are enrolled in the PhD Program and you will graduate in the year {int(roll[0:4])+5}.")
else:
    print("Please enter a valid Roll Number.")