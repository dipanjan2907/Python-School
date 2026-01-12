#Create a CSV file storing daily temperature data (Date, Max Temp, Min Temp). Write a program to:
#Calculate the hottest and coldest days.
#Find all dates where the temperature difference (Max - Min) was more than 10°C.
import csv
def inputs():
    with open ("temp.csv",'w',newline='') as obj:
        f=csv.writer(obj)
        f.writerow(['Date', 'Max_Temp','Min_Temp'])
        while True:
            d=input("Enter Date: ")
            max=int(input("Max Temp in ℃: "))
            min=int(input("Min Temp in ℃: "))
            f.writerow([d,max,min])
            ch=int(input("1. More\n2. Stop\n1/2?: "))
            if ch==2:
                print("All Data Inputted.")
                break
def ops():
    with open ("temp.csv",'r') as f:
        data1=csv.reader(f)
        next(f)
        hot,cold=0,90
        diff=[]
        for i in data1:
            if hot<int(i[1]):
                hot=int(i[1])
                hotd=[i[0],hot]
            if cold>int(i[2]):
                cold=int(i[2])
                coldd=[i[0],cold]
            if (int(i[1])-int(i[2]))>10:
                diff.append([i[0],int(i[1])-int(i[2])])
        print(f"Hottest Day on {hotd[0]} with temp {hotd[1]} ℃")
        print(f"Coldest Day on {coldd[0]} with temp {coldd[1]} ℃")
        print("Days with Temp difference greater than 10 ℃")
        for i in diff:
            print(f"On {i[0]} with temp diff {i[1]} ℃")
while True:
    ch=int(input("1. Input Data\n2. Show Operations Performed\n3. Exit\n1/2/3? :"))
    if ch in [1,2]:
        if ch==1:
            inputs()
        elif ch==2:
            ops()
    elif ch==3:
        print("Exiting...")
        break