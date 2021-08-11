string=input("3x3 or 2x2")
if(string=='2x2'):
    def multiply2(x,y):
        for i in range(0,2):
            for j in range(0,2):
                prodlist[i][j]=0.0
                for k in range(0,2):
                    prodlist[i][j]=prodlist[i][j]+(listA[k][i]*listB[j][k])
        return prodlist
    prodlist=[[0,0],[0,0]]
    list1=[]
    list2=[]
    list3=[]
    list4=[]
    listA=[list1, list2]
    listB=[list3, list4]
    print("Enter elements of matrix 1")
    for i in range(0,2):
        list1.append(float(input(" ")))
    for i in range(2,4):
        list2.append(float(input(" ")))
    print("enter elements of 2nd matrix")
    for j in range(0,2):
        list3.append(float(input(" ")))
    for j in range(2,4):
        list4.append(float(input(" ")))
    print(multiply2(listA,listB))
else:
    def multiply3(x,y):
        for i in  range(0,3):
            for j in range(0,3):
                prodlist[i][j]=0.00
                for k in range(0,3):
                    prodlist[i][j]=prodlist[i][j]+(list1)[k][i]*list2[j][k]
        return prodlist
    prodlist=[[0,0,0],[0,0,0],[0,0,0]]
    list_a=[]
    list_b=[]
    list_c=[]
    list_d=[]
    list_e=[]
    list_f=[]
    list1=[list_a,list_b,list_c]
    list2=[list_d,list_e,list_f]
    print("Enter elements of matrix1")
    for i in range(0,3):
        list_a.append(float(input(" ")))
    for i in range(3,6):
        list_b.append(float(input(" ")))
    for i in range(6,9):
        list_c.append(float(input(" ")))
    for j in range(0,3):
        list_d.append(float(input(" ")))
    for j in range(3, 6):
        list_e.append(float(input(" ")))
    for j in range(6,9):
        list_f.append(float(input(" ")))
    print(multiply3(list1,list2))