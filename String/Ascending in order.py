w=input("Enter a word: ")
flag=0
for i in range(1,len(w)):
    if ord(w[i-1])<ord(w[i]):
        flag=1
    else:
        flag=0
        break
if flag==1:
    print("Ascending in order")
else:
    print("Not Ascending in order")
