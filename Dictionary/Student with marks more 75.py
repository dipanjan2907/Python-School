d={}
l=int(input("Enter Limit: "))
for i in range(0,l):
    r=int(input("Roll: "))
    n=input("Name: ")
    m=int(input("Marks(%): "))
    d[r]=[n,m]
print("Student Details with MARKS ABOVE 75%\n")
for i,j in d.items():
    if j[1]>75:
        print(f"Roll: {i}\nName: {j[0]}\nMarks: {j[1]}")