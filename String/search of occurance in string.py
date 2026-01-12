def FindWord(String,Search):
    l1=[]
    c=0
    l1=String.split()
    for i in l1:
        if i.capitalize()==Search.capitalize():
            c+=1
    return c
String=input("Enter the string: ")
Search=input("Enter the word to be searched: ")
print(f"There are {FindWord(String,Search)} occurences of the word {Search} in the string {String}")