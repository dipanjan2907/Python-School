s=input("Enter word: ")
s=s.upper()
s1=s[::-1]
print(s1)
if(s==s1):
    print("Palindrome")
else:
    print("Not Palindrome")
