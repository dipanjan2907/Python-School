l1 = ['A', 'B', 'C', 'D', 'E']
s = 4
l = 1
for i in range(1, 6):
    for j in range(1, s + 1):
        print("  ", end=" ")
    for k in range(0,l):
        print(l1[k], end=" ")
    s -= 1
    l += 1
    if i > 1:
        for m in range(0, i):
            print(l1[m], end=" ")
        print(" ")
    else:
        print(" ")
