s = input("Enter String: ").strip()
c = 0
if s.count(' ') == 0:
    print("String is of one word only.")
    c = 1
elif s == s.title():
    print("String is already in title case.")
    c = 1
else:
    for i in range(1, len(s)):
        if s[i - 1] != " " and s[i].isupper():
            print("No Space, only  first character to be in upper case.")
            c = 1
            break
if c == 0:
    s = s.title()
    print(s)
