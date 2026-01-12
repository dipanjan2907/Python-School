i=1
with open('Gratitude.txt', 'r') as f:
    while True:
        l=f.readline()
        if not l:
            break
        print(f"Line {i}: {l.lower().count('e')} e's")
        i+=1
with open('Gratitude.txt', 'r') as f:
    while True:
        l=f.readline()
        if not l:
            break
        if l[0]=='I':
            print(l)
        else:
            continue