l1=[['Harry Potter','J.K.Rowling'],['To Kill a Mockingbird','Harper Lee'],['Fantastic Beasts','J.K.Rowling']]
l=int(input("Enter the number of books you want to push: "))
for i in range(l):
    n=input("Enter the book name: ").title()
    a=input("Enter the author name: ").title()
    l1.append([n,a])
def push_book(l1):
    bk=[]
    for i in range(len(l1)):
        if l1[i][1]=='J.K.Rowling':
            bk.append(l1[i][0])
    return bk
def pop_book():
    lbk=push_book(l1)
    while len(lbk)!=0:
            print(lbk.pop())
    print("Underflow")
pop_book()
push_book(l1)
