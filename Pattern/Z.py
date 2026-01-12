a=int(input("ENTER LENGTH: "))
for i in range(1,a+1):
        if (i==1 or i==a):
            print("*"*a)
        else:
            print(" "*(a-i)+"*")
   