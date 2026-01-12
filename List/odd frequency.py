n=int(input("How many?: "))
l1=[1,4,3,7,2,3,8,4,1,2,1,7,2,7,8]
'''for i in range(0,n):
    l1.append(int(input("No.: ")))'''
for i in l1:
    c=l1.count(i)
    if c%2!=0:
        print(i," = ",c)
        l1.remove(i)