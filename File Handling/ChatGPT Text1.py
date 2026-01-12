#The total number of words in the file.
#The number of lines that contain the word "Python".
def write():
    with open("Practice.txt","w") as f:
        while True:
            str=input("Enter the complete line to write into file:\n")
            f.write(f"{str}\n")
            ch=int(input("1. Continue Writing\n2. Exit\n1 or 2?: "))
            if ch==2:
                break
def wordnumber():
    c,l,ln=0,0,0
    ls=[]
    with open("Practice.txt","r") as f:
        while True:
            data=f.readline()
            if not data:
                break
            ln+=1
            wordlist=[]
            wordlist=data.split(" ")
            if "Python" in wordlist:
                l+=1
                ls.append(ln)
            c+=len(wordlist)
            
        print(f"There are {c} words.")
        print(f"{l} lines have 'Python'. Line Numbers- {ls}") 
def append():
    with open("Practice.txt","a") as f:
        while True:
            str=input("Enter the complete line to write into file:\n")
            f.write(f"{str}\n")
            ch=int(input("1. Continue Writing\n2. Exit\n1 or 2?: "))
            if ch==2:
                break
    with open("Practice.txt","r") as f:
        data=f.read().split('\n')
        data=data[-4:-1]
        print("\nLast 3 lines:")
        for i in data:
            print(i)

#append()
#write()
#wordnumber()