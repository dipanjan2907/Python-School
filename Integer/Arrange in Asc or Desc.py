n1=int(input("Enter number: "))
n2=int(input("Enter number: "))
n3=int(input("Enter number: "))
c=int(input("To arrange in Descending enter 1, for Ascending enter 2: "))
if(c==1):
    if n1 > n2 and n1 > n3:
        print(n1, end=", ")
        if n2 > n3:
            print(n2, end=", ")
            print(n3, end=", ")
        else:
            print(n3, end=", ")
            print(n2, end=", ")
    elif n2 > n1 and n2 > n3:
        print(n2, end=", ")
        if n1 > n3:
            print(n1, end=", ")
            print(n3, end=", ")
        else:
            print(n3, end=", ")
            print(n1, end=", ")
    else:
        print(n3, end=", ")
        if n1 > n2:
            print(n1, end=", ")
        
            print(n2, end=", ")
        else:
            print(n2, end=", ")
            print(n1, end=", ")
elif(c==2):
    if n1 < n2 and n1 < n3:
        print(n1, end=", ")
        if n2 < n3:
            print(n2, end=", ")
            print(n3, end=", ")
        else:
            print(n3, end=", ")
            print(n2, end=", ")
    elif n2 < n1 and n2 < n3:
        print(n2, end=", ")
        if n1 < n3:
            print(n1, end=", ")
            print(n3, end=", ")
        else:
            print(n3, end=", ")
            print(n1, end=", ")
    else:
        print(n3, end=", ")
        if n1 < n2:
            print(n1, end=", ")
            print(n2, end=", ")
        else:
            print(n2, end=", ")
            print(n1, end=", ")

else:
    print("INVALID CHOICE!")