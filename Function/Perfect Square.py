num=int(input("Enter number: "))
def PerfSquare(n):
    for i in range(1,n//2):
        if(i**2==n):
            print("Perfect Square.")
            break
        else:
            n1=n
            while(i**2!=n):
                n+=1
                for i in range(1,n//2):
                    if(i**2==n):
                        print("Not a Perfect Square. ",(n-n1)," need to added to get the Nearest Perfect Square ",n)
                        break
        break
PerfSquare(num)