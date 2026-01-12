k = 1
l = 2
for i in range(1, 4):
    for m in range(l, 0, -1):
        print(" ", end=" ")
    for j in range(1, k + 1):
        print("*", end=" ")
    print(" ")
    l -= 1
    k += 2

l = 2
k = 3
for i in range(1, 3):
    for m in range(l, 1, -1):
        print(" ", end=" ")
    for j in range(1, k + 1):
        print("*", end=" ")
    print(" ")
    l += 1
    k -= 2
