import csv
def add_ebook():
    with open('ebook.csv') as f:
        o=csv.writer(f)
        o.writerow(['ebook_ID','Title','Author','Genre','Price'])
        while True:
            ebook_ID=input("Enter ebook_ID: ")
            Title=input("Enter Title: ")
            Author=input("Enter Author: ")
            Genre=input("Enter Genre: ")
            Price=input("Enter Price: ")
            o.writerow([ebook_ID,Title,Author,Genre,Price])
            ch=input("Do you want to add more ebooks? (y/n): ")
            if ch=='n':
                break
def search_genre():
    with open('ebook.csv') as f:
        r=csv.reader(f)
        genre=input("Enter the genre: ")
        for row in r:
            if row[3]==genre:
                print(row)