def countvowels():
    with open("Word.txt",'r') as f:
        c=0
        d=f.read()
        for i in d:
            if i.lower() in "aeiou":
                c+=1
    return c
print(f"Number of vowels: {countvowels()}")