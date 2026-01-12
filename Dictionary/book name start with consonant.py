def dispBook(BOOKS):
    for i in BOOKS.values():
        if i[0] not in 'AEIOU':
            print(i)
BOOKS={}
l=int(input("Enter the number of books: "))
for i in range(l):
    name=input("Enter the name of the book: ").capitalize()
    BOOKS[i]=name
dispBook(BOOKS)