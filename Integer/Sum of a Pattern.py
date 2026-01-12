n=int(input("Enter limit (n): "))
s=0
for i in range(1,n+1):
    s=s+(i/((i*i)+1))
print("Series is 1/2 + 2/5 +.....+ n/(n*n)+1")
print("SUM= ",s)