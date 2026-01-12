review=input("Enter Review: ")
review=" "+review+" "
c=0
w=""
for i in range(0,len(review)):
    if review[i] == " ":
        if w == "good":
            c += 1
        w=""
    elif review[i] != " ":
        w += review[i] 
print(c)