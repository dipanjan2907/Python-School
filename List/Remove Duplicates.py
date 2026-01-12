l=int(input("How many numbers to enter?: "))
l1=[]
for i in range(1,l+1):
      n=int(input("Enter number: "))
      l1.append(n)
print("Original= ",l1)
for i in l1:
      c=l1.count(i)
      while(c>1):
          l1.remove(i)
          c-=1
print("Duplicates Removed= ",l1)
      
