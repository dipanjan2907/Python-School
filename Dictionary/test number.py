Stu_dict={}
Stu_stk=[]
l=int(input("Enter the number of students: "))
for i in range(l):
    Stu_id=input("Enter the student id: ")
    ts1=int(input("Enter Marks for 1st Test: "))
    ts2=int(input("Enter Marks for 2nd Test: "))
    ts3=int(input("Enter Marks for 3rd Test: "))
    Stu_dict[Stu_id]=(ts1,ts2,ts3)
def Push_elements(Stu_Stk, Stu_dict):
    for i in Stu_dict:
        if Stu_dict[i][2]>=80:
            Stu_stk.append(i)
    return Stu_stk
def Pop_elements(Stu_stk):
    while len(Stu_stk)>0:
        print(Stu_stk.pop())
    print("Stack Empty")
Push_elements(Stu_stk, Stu_dict)
Pop_elements(Stu_stk)
