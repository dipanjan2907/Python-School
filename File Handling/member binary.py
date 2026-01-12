import pickle
f=open("member.dat","ab+")
l=int(input("How many members?: "))
for i in range(0,l):
    m=int(input("Enter member no.: "))
    n=input("Enter member name: ")
    member={'MemberNo.':m,'Name ':n}
    pickle.dump(member,f)
f.close()
f=open("member.dat","rb")
while True:
    try:
        me=pickle.load(f)
        print(me)
    except EOFError:
        break
f.close()

'''while True:
            try:
                member = pickle.load(f)
                if member['MemberNo.'] == member_no:
                    print(f"Member found: {member}")
                    found = True
                    break
            except EOFError:
                break'''