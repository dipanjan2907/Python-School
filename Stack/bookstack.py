def push_book(BookStack,new_book):
    BookStack.append(new_book)
    print(f"Book '{new_book[0]}' registered..")
def pop_book(BookStack):
    if(len(BookStack)==0):
        print("UNDERFLOW..")
    else:
        p=BookStack.pop()
        print(f"Book '{p[0]}' popped..")
        return p
def peep(BookStack):
    if(len(BookStack)==0):
        print("NONE..")
    else:
        p=BookStack[-1]
        print(f"Topmost Book: '{p[0]}' written by '{p[1]}' in {p[2]}")
        return p
BooksStack=[]
c='y'
while c=='y':
    n=input("Enter Book's Name: ")
    a=input("Enter the Author's Name: ")
    y=int(input("Year Published: "))
    if n == "" or a == "" or y == "" or n.isspace() or a.isspace() or y<1:
        print("White Space not allowed.")
    else:
        l=[n,a,y]
        push_book(BooksStack,l)
    c=input("ADD MORE (y/n): ").lower()
pop_book(BooksStack)
peep(BooksStack)