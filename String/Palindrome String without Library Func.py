w=input("Enter word: ")
w=w.lower()
w1=""
for i in range(len(w)-1,-1,-1):
    w1+=w[i]
print(w1)
if w==w1:
    print("Palindrome.")
else:
    print("Not Palindrome.")