print("1.ADD")
print("2.SUBSTRACT")
print("3.MULTIPLY")
print("4.DIVIDE")
choice=int(input("Enter your choice: "))
n1=int(input("Enter 1st number: "))
n2=int(input("Enter 2nd number: "))
match choice:
           case 1:print(n1+n2)
           case 2:
            if n1>n2:
             print(n1-n2)
            else:
             print(n2-n1)
           case 3:print(n1*n2)
           case 4:print(n1/n2)
           case default:print("INVALID choice")
