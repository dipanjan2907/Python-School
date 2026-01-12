with open ('Text.txt','r') as f:
    d=f.read()
    while True:    
        c=0
        print('1. Vowels\n2. Consonants\n3. Upper Case\n4. Lower Case\n5. Exit')
        ch=int(input('Enter your choice (1/2/3/4/5): '))
        if ch==5:
            print("EXITTED")
            break
        try:
            for i in d:
                if i.isalpha():
                    if ch==1:
                        if i in 'AEIOUaeiou':
                            c+=1
                            t='Vowel'
                    elif ch==2:
                        if i not in 'AEIOUaeiou':
                            c+=1
                            t='Consonants'
                    elif ch==3:
                        if i.isupper():
                            c+=1
                            t='Upper Case'
                    elif ch==4:
                        if i.islower():
                            c+=1
                            t='Lower Case'
        except FileExistsError as e:
            print(f"{e}")
        print(f"{t} = {c}\n")