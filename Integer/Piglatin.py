w=input("Enter word: ")
w=w.upper()
for i in range(0,len(w)):
    if(w[i]=='A' or w[i]=='E' or w[i]=='I' or w[i]=='O' or w[i]=='U'):
        w1=w[0:i]
        break
print("Piglatin form: ",(w[i:len(w)]+w1+"AY"))