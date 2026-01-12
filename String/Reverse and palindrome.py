w=input("Enter a word: ")
w=w.upper()
t=""
for i in range(len(w)-1,0-1,-1):
    t=t+w[i]
print("Reverse of ",w," is ",t)
if w==t:
    print(w," is a Palindrome word.")
else:
    print(w," is not a Palindrome word.")
