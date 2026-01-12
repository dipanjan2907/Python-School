def key_press(s):
    d1={1:[' '],
        2:['a','b','c'],
        3:['d','e','f'],
        4:['g','h','i'],
        5:['j','k','l'],
        6:['m','n','o'],
        7:['p','q','r','s'],
        8:['t','u','v'],
        9:['w','x','y','z'],
        0:['_']}
    c=0
    for l in s:
        if l.isupper():
            c+=1
        for i, j in d1.items():
            if l.lower() in j:
                c+=j.index(l.lower())+1
                break
    return c-1
s=input("Enter the string: ")
print(f"Total Key Strokes: {key_press(s)}")
            
